from django.http.response import Http404, JsonResponse
from django.views.generic import TemplateView

from application.models import bnb, BnbInformation
from application.models.bnb import Image
from application.services.owner_management_service import (get_info_owner, get_list_info_bnb,
                                                           get_bnb_by_id, get_list_category,
                                                           get_list_service, get_list_rule, get_bnb)

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
        owner, list_bnb = self.get_info_owner_data(userid)
        context['owner'] = owner  # Đưa dữ liệu vào context
        context['list_bnb'] = list_bnb
        context['categories'] = get_list_category()
        context['services'] = get_list_service()
        context['rules'] = get_list_rule()
        return context

    def get_info_owner_data(self, userid):
        # Gọi dịch vụ để lấy thông tin chủ nhà
        owner = get_info_owner(userid)
        if owner is None:
            raise Http404("Eooooo, tìm nhầm chỗ rồi.")  # Không tìm thấy chủ nhà
        list_bnb = get_list_info_bnb(owner.get("id"))
        return owner, list_bnb


class UpdateBnBView(TemplateView):
    template_name = "manage_of_owner/form-bnb.html"

    def post(self, request, *args, **kwargs):
        # Lấy dữ liệu từ form
        name = request.POST.get('name', '')
        delete_img = request.POST.getlist('delete-image', [])
        add_img = request.FILES.getlist('add-image')
        price = request.POST.get('price', 0)
        capacity = request.POST.get('capacity', 0)
        category_id = request.POST.getlist('category-id', [])
        service_id = request.POST.getlist('service-id', [])
        service_id = request.POST.getlist('rule-id', [])
        description = request.POST.get('description', '')
        bnbid = request.POST.get('bnbid', -1)
        print(add_img)

        try:
            # Cập nhật thông tin BnB
            bnb = get_bnb(bnbid)
            if bnb is None:
                return JsonResponse({'success': False})
            bnb.name = name
            bnb.description = description
            bnb.price = price
            bnb.capacity = capacity
            for i in delete_img:
                # Lấy hình ảnh cụ thể và xóa nó
                image_to_delete = bnb.image_set.get(id=i)  # Lấy hình ảnh có ID tương ứng
                image_to_delete.delete()  # Xóa hình ảnh
            for img in add_img:
                print(img.url)
                # Tạo đối tượng Image mới cho mỗi tệp hình ảnh
                image_to_add = Image(url=img.url, product=bnb)
                image_to_add.save()  # Lưu đối tượng Image vào cơ sở dữ liệu
            bnb.save()
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
