from django.views.generic import TemplateView
from django.http import Http404, JsonResponse
from application.services.search_service import get_bnb_result_info,get_bnb_result
class ResultView(TemplateView):
    template_name = "application/templates/search-result.html"

    def get_context_data(self, searchkey, **kwargs):
        context = super().get_context_data(**kwargs)
        # Tìm theo tên nhà
        context['searchkey'] =[get_bnb_result_info(bnb_id) for bnb_id in get_bnb_result(searchkey)]
        return context
