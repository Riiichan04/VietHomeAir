from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from application.models import BnbInformation

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

        # Chuẩn bị context
        context = {
            'bnb': bnb,
            'checkin': checkin,
            'checkout': checkout,
            'capacity': capacity,
            'images': images,
            'owner_name': owner_name,  # Truyền tên chủ nhà vào context
            'owner_avatar': owner_avatar,  # Truyền hình ảnh chủ nhà vào context
            'price_per_night': bnb.price,  # Lấy giá sản phẩm
        }

        return render(request, self.template_name, context)
