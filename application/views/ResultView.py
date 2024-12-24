from django.views.generic import TemplateView
from django.http import Http404, JsonResponse

from application.models import BnbInformation
from application.services.search_service import get_bnb_result_info,get_bnb_result
class ResultView(TemplateView):
    template_name = "application/templates/search-result.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.kwargs.get('query', '')
        results = get_bnb_result(query)
        context['results'] = results
        return context
        # Tìm theo tên nhà
        # context['query'] =[get_bnb_result_info(bnb_id) for bnb_id in get_bnb_result(query)]

