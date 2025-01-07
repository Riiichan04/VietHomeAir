from django.views.generic import TemplateView
from django.http import Http404, JsonResponse
from application.services.search_service import get_search, get_bnb_by_result
class ResultView(TemplateView):
    template_name = "application/templates/search-result.html"

    def get_context_data(self, **kwargs):
        query = self.kwargs['query']
        results= get_search(query)
        if not results:
            raise Http404("Hả")
        list_bnb = get_bnb_by_result(query)
        context = super().get_context_data(**kwargs)
        context['list_bnb'] = list_bnb
        return context

