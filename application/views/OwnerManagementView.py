import json

from cloudinary.uploader import upload
from django.http.response import Http404, JsonResponse
from django.views.generic import TemplateView
from application.models.bnb import Image, Category, Service, Rule
from application.services.owner_management_service import (get_info_owner, get_list_info_bnb,
                                                           get_bnb_by_id, get_list_category,
                                                           get_list_service, get_list_rule,
                                                           get_bnb, get_bnb_reviews, get_list_info_bnb_avg_rating,
                                                           get_booking_bnb, get_booking_by_id)

class OwnerManagementView(TemplateView):
    template_name = 'manage_of_owner/base.html'

    def get_context_data(self, **kwargs):
        # Gọi phương thức cha để lấy context ban đầu
        context = super().get_context_data(**kwargs)

        # Kiểm tra nếu có 'bnbid' trong kwargs
        bnbid = self.kwargs.get('bnbid')
        if bnbid:
            bnb = get_bnb_by_id(bnbid)
            if bnb is None:
                raise Http404("BnB không tồn tại.")
            context['bnb'] = bnb

        # Lấy userid từ session
        userid = self.request.session.get('user')

        # Kiểm tra nếu không có userid trong session
        if not userid:
            raise Http404("Không tìm thấy thông tin người dùng.")

        # Lấy thông tin chủ nhà từ userid
        owner, list_bnb, list_booking = self.get_info_owner_data(userid)
        context['owner'] = owner  # Đưa dữ liệu vào context
        context['list_bnb'] = list_bnb
        context['list_booking'] = list_booking
        context['categories'] = get_list_category()
        context['services'] = get_list_service()
        context['rules'] = get_list_rule()
        context['bnb_reviews'] = get_bnb_reviews(owner.get("id"))
        context['list_bnb_avg'] = get_list_info_bnb_avg_rating(owner.get("id"))
        return context

    def get_info_owner_data(self, userid):
        # Gọi dịch vụ để lấy thông tin chủ nhà
        owner = get_info_owner(userid)
        if owner is None:
            raise Http404("Eooooo, tìm nhầm chỗ rồi.")  # Không tìm thấy chủ nhà
        list_bnb = get_list_info_bnb(owner.get("id"))
        list_booking = get_booking_bnb(list_bnb)
        return owner, list_bnb, list_booking



class UpdateBnBView(TemplateView):
    template_name = "manage_of_owner/form-bnb.html"

    def post(self, request, *args, **kwargs):

        # Lấy userid từ session
        userid = self.request.session.get('user')

        # Kiểm tra nếu không có userid trong session
        if not userid:
            raise Http404("Không tìm thấy thông tin người dùng.")

        # Lấy dữ liệu từ form
        name = request.POST.get('name', '')
        delete_img = request.POST.getlist('delete-image', [])
        add_img = request.FILES.getlist('add-image')
        price = request.POST.get('price', 0)
        capacity = request.POST.get('capacity', 0)
        category_id = request.POST.getlist('category-id', [])
        service_id = request.POST.getlist('service-id', [])
        rule_id = request.POST.getlist('rule-id', [])
        description = request.POST.get('description', '')
        bnbid = request.POST.get('bnbid', -1)

        try:
            # Cập nhật thông tin BnB
            bnb = get_bnb(bnbid)
            if bnb is None:
                return JsonResponse({'success': False})

            bnb.name = name
            bnb.description = description
            if float(price) >= 0:
                bnb.price = price
            if int(capacity) >= 0:
                bnb.capacity = capacity

            #xóa hình ảnh
            for i in delete_img:
                # Lấy hình ảnh cụ thể và xóa nó
                image_to_delete = bnb.image_set.get(id=i)  # Lấy hình ảnh có ID tương ứng
                image_to_delete.delete()

            #thêm hình ảnh
            for file in add_img:

                # Tải tệp lên Cloudinary và nhận URL
                cloudinary_response = upload(file)
                file_url = cloudinary_response['secure_url']  # Lấy URL an toàn

                print(file_url)
                # Tạo đối tượng Image mới cho mỗi tệp hình ảnh
                image_to_add = Image(url=file_url, product=bnb)
                image_to_add.save()  # Lưu đối tượng Image vào cơ sở dữ liệu

            #xóa category cũ trong bnb
            bnb.category.clear()
            #thêm category vào lại
            for cid in category_id:
                category = Category.objects.get(id=cid)  # Lấy category theo id
                if not bnb.category.filter(id=cid).exists():  # Kiểm tra nếu chưa tồn tại
                    bnb.category.add(category)  # Thêm category vào bnb

            #xóa service cũ trong bnb
            bnb.service.clear()
            #thêm service vào lại
            for sid in service_id:
                service = Service.objects.get(id=sid)
                if not bnb.service.filter(id=sid).exists():
                    bnb.service.add(service)

            # xóa service cũ trong bnb
            bnb.rule.clear()
            # thêm service vào lại
            for rid in rule_id:
                rule = Rule.objects.get(id=rid)
                if not bnb.rule.filter(id=rid).exists():
                    bnb.rule.add(rule)

            bnb.save()
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

class AcceptBookingView(TemplateView):
    template_name = "manage_of_owner/owner-management-dashboard.html"
    def post(self, request, *args, **kwargs):
        # Parse dữ liệu JSON từ request body
        data = json.loads(request.body)
        booking_id = data.get('bookingId')
        status = data.get('status')
        print(booking_id)
        try:
            booking = get_booking_by_id(booking_id)
            if booking is None:
                return JsonResponse({'success': False})
            if status == 'accept':
                booking.status = 'accept'
            if status == 'decline':
                booking.status = 'decline'
            if status == 'served':
                booking.status = 'served'
            booking.save()
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
