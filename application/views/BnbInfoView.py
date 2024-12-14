from django.http import Http404
from django.views.generic import TemplateView
from application.models import BnbInformation
import application.module.bnb_processing as bnb_processing


class SampleBnbInfoView(TemplateView):
    template_name = "application/templates/bnb-information.html"


class BnbInfoView(TemplateView):
    template_name = "application/templates/bnb-information.html"

    def get_context_data(self, **kwargs):
        bnb = bnb_processing.get_bnb(self.kwargs['bnbid'])
        if bnb is None: raise Http404()
        context = super().get_context_data(**kwargs)
        context['bnb'] = bnb
        return context