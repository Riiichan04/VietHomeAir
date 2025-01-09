import json
from datetime import datetime

from django.http import JsonResponse, Http404
from django.utils.dateparse import parse_datetime
from django.views.generic import TemplateView
from django.shortcuts import render
import application.services.bnb_info_service as bnb_service
from application.models import BnbInformation, Account
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
            raise Http404("Eooooo, tìm nhầm chỗ rồi")

        # Xử lý dữ liệu
        try:
            bnb = bnb_service.get_bnb_info(bnb_id)
        except BnbInformation.DoesNotExist:
            raise Http404("Eooooo, tìm nhầm chỗ rồi")

        # Lấy danh sách hình ảnh liên quan đến BnbInformation
        images = bnb['images']

        # Lấy thông tin chủ nhà từ BnbInformation
        owner_name = bnb['owner'].fullname
        owner_avatar = bnb['owner'].avatar
        price_per_night = bnb['prices']  # Lấy giá từ BnbInformation

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


class HandleNewReview(TemplateView):
    def post(self, request, **kwargs):

        # Lấy dữ liệu từ request
        user_id = request.POST.get('user')
        bnb_id = request.POST.get('bnb_id')
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        capacity = int(request.POST.get('capacity'))

        # Kiểm tra dữ liệu đầu vào
        if not all([bnb_id, checkin, checkout, capacity]):
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

        user = Account.objects.filter(id=int(user_id)).first()

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
