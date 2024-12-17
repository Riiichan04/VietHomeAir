from django.http import Http404
from django.views.generic import TemplateView
from application.models import BnbInformation
import application.services.bnb_info_service as bnb_service


class SampleBnbInfoView(TemplateView):
    template_name = "application/templates/bnb-information.html"


class BnbInfoView(TemplateView):
    template_name = "application/templates/bnb-information.html"

    def get_context_data(self, **kwargs):
        bnb = bnb_service.get_full_bnb_info(self.kwargs['bnbid'])
        if bnb['bnb_info'] is None: raise Http404("Eooooo, tìm nhầm chỗ rồi")
        context = super().get_context_data(**kwargs)
        # Code tạm để mai báo cáo
        context['title'] = bnb['bnb_info'].name
        context['images'] = [image.url for image in bnb['images']]
        context['price'] = '{0:,}'.format(bnb['bnb_info'].price).replace('.00', '').replace(',', '.')
        context['default_calculated_price'] = '{0:,}'.format(bnb['bnb_info'].price*5).replace('.00', '').replace(',', '.')    #Sẽ chỉnh sau
        context['default_final_price'] = '{0:,}'.format(bnb['bnb_info'].price*5 + 70000).replace('.00', '').replace(',', '.')    #Sẽ chỉnh sau
        context['description'] = bnb['bnb_info'].description
        context['service'] = ''.join(list(["- " + service.name + '\n' for service in bnb['services']]))
        context['rule'] = [rule.description for rule in bnb['rules']]
        context['reviews'] = [review for review in bnb['reviews']]
        context['owner'] = bnb['owner']
        return context