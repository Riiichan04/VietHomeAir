from django import template

from django.http import Http404
from django.views.generic import TemplateView
from application.models import BnbInformation
import application.services.bnb_info_service as bnb_service

class BnbInfoView(TemplateView):
    template_name = "application/templates/bnb-information.html"


    def get_context_data(self, **kwargs):
        bnb = bnb_service.get_bnb_info(self.kwargs['bnbid'])
        if bnb is None: raise Http404("Eooooo, tìm nhầm chỗ rồi")
        context = super().get_context_data(**kwargs)
        context['bnb'] = bnb
        return context