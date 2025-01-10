from django.views.generic import TemplateView

from application.models import BnbInformation
from application.services.home_service import get_bnb_display_element, get_most_viewed_bnb, get_most_rated_bnb


class HomeView(TemplateView):
    template_name = "application/templates/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hotbnb'] = [get_bnb_display_element(bnb_id) for bnb_id in get_most_viewed_bnb()]
        context['high_rated_bnb'] = [get_bnb_display_element(bnb_id) for bnb_id in get_most_rated_bnb()]
        context['other_bnb'] = [get_bnb_display_element(bnb_id) for bnb_id in
                               range(1, len(BnbInformation.objects.all()) + 1 if len(BnbInformation.objects.all()) + 1 < 40 else 40)]
        return context
