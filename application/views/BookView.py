import json
from datetime import datetime

from django.http import JsonResponse
from django.utils.timezone import make_aware
from django.utils.dateparse import parse_datetime
from django.views.generic import TemplateView
from django.shortcuts import render
from application.models import BnbInformation
from application.models.accounts import Booking
from application.models.bnb import Image

class BookView(TemplateView):
    template_name = 'application/templates/booking.html'

    def get(self, request, *args, **kwargs):
        # Lấy tham số từ query parameters
        bnb_id = request.GET.get('bnbid')
        checkin = request.GET.get('checkin')
        checkout = request.GET.get('checkout')
        capacity = request.GET.get('capacity')

        # Kiểm tra các tham số bắt buộc
        if not all([bnb_id, checkin, checkout, capacity]):
            return render(request, 'error.html', {'message': 'Missing required query parameters.'})

        # Xử lý dữ liệu
        try:
            bnb = BnbInformation.objects.get(id=bnb_id, status=True)
        except BnbInformation.DoesNotExist:
            return render(request, 'error.html', {'message': 'No such BnB found.'})

        # Lấy danh sách hình ảnh liên quan đến BnbInformation
        images = Image.objects.filter(product=bnb)

        # Lấy thông tin chủ nhà từ BnbInformation
        owner = bnb.owner  # Lấy đối tượng Owner liên kết với BnbInformation
        owner_name = owner.account.fullname if owner else None
        owner_avatar = owner.account.avatar if owner else None
        price_per_night = bnb.price  # Lấy giá từ BnbInformation

        # Chuẩn bị context
        context = {
            'bnb': bnb,
            'checkin': checkin,
            'checkout': checkout,
            'capacity': capacity,
            'images': images,
            'owner_name': owner_name,  # Truyền tên chủ nhà vào context
            'owner_avatar': owner_avatar,  # Truyền hình ảnh chủ nhà vào context
            'price_per_night': price_per_night,  # Truyền giá vào context
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)

            # Lấy dữ liệu từ request
            bnb_id = data.get('bnb_id')
            checkin = data.get('checkin')
            checkout = data.get('checkout')
            capacity = data.get('capacity')
            cccd = data.get('cccd')  # Nhận thêm CCCD từ request

            # Kiểm tra dữ liệu đầu vào
            if not all([bnb_id, checkin, checkout, capacity, cccd]):
                return JsonResponse({'result': False, 'message': 'Thiếu dữ liệu bắt buộc.'}, status=400)

            # Kiểm tra BnB tồn tại
            try:
                bnb = BnbInformation.objects.get(id=bnb_id)
            except BnbInformation.DoesNotExist:
                return JsonResponse({'result': False, 'message': 'BnB không tồn tại.'}, status=404)

            # Chuyển đổi ngày tháng từ chuỗi sang đối tượng DateTime
            checkin_date = parse_datetime(checkin)
            checkout_date = parse_datetime(checkout)

            if checkin_date >= checkout_date:
                return JsonResponse({'result': False, 'message': 'Ngày check-out phải sau ngày check-in.'}, status=400)

            # Kiểm tra capacity hợp lệ
            if not isinstance(capacity, int) or capacity <= 0:
                return JsonResponse({'result': False, 'message': 'Số người ở phải là một số hợp lệ.'}, status=400)

            # Kiểm tra trùng booking
            overlapping_booking = Booking.objects.filter(
                bnb=bnb,
                from_date__lt=checkout_date,
                to_date__gt=checkin_date
            )
            if overlapping_booking.exists():
                return JsonResponse({'result': False, 'message': 'BnB đã được đặt trong khoảng thời gian này.'},
                                    status=400)

            # Tìm người dùng theo CCCD
            try:
                user = request.user.account  # Assuming request.user has account attribute
            except AttributeError:
                return JsonResponse({'result': False, 'message': 'User not found.'}, status=404)

            # Lưu thông tin đặt phòng
            booking = Booking.objects.create(
                account=user,
                bnb=bnb,
                from_date=checkin_date,
                to_date=checkout_date,
                capacity=capacity,
                status='pending'
            )
            booking.save()

            return JsonResponse({'result': True, 'message': 'Đặt phòng thành công!', 'bnb_id': booking.id})

        except Exception as e:
            return JsonResponse({'result': False, 'message': f'Lỗi hệ thống: {str(e)}'}, status=500)
