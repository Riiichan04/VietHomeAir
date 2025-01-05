from django.views.generic import TemplateView
from django.http import Http404, JsonResponse
from application.services.home_service import get_bnb_display_element
from application.models import BnbInformation
class ResultView(TemplateView):
    template_name = "application/templates/search-result.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.kwargs.get('query')
        # results = get_bnb_result(query)
        # context['results'] = results
        results= BnbInformation.objects.filter(name__contains=query).all()
        list_bnb = [get_bnb_display_element(result.id) for result in results]
        context['list_bnb'] = list_bnb
        return context
        # Tìm theo tên nhà
        # context['query'] =[get_bnb_result_info(bnb_id) for bnb_id in get_bnb_result(query)]

    # def get(self, request, *args, **kwargs):

