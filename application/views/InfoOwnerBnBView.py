from django.http import Http404
from django.views.generic import TemplateView
from application.services.info_owner_service import (get_info_owner, get_bnb_reviews, get_list_info_bnb_avg_rating)

class InfoOwnerBnBView(TemplateView):
    template_name = "application/templates/info-owner-bnb.html"

    def get_context_data(self, **kwargs):
        context = super(InfoOwnerBnBView, self).get_context_data(**kwargs)

        owner_id = self.kwargs.get('ownerid')
        if owner_id is None:
            raise Http404("Eooooo, tìm nhầm chỗ rồi.")
        owner = self.get_info_owner_data(owner_id)
        if owner is None:
            raise Http404("Eooooo, tìm nhầm chỗ rồi.")
        context['owner'] = owner  # Đưa dữ liệu vào context
        context['list_bnb_avg'] = get_list_info_bnb_avg_rating(owner.get("id"))
        context['bnb_reviews'] = get_bnb_reviews(owner.get("id"))
        return context

    def get_info_owner_data(self, userid):
         # Gọi dịch vụ để lấy thông tin chủ nhà
        owner = get_info_owner(userid)
        if owner is None:
            raise Http404("Eooooo, tìm nhầm chỗ rồi.")  # Không tìm thấy chủ nhà
        return owner