from django.views.generic import TemplateView
from django.http import Http404, JsonResponse
from application.services.search_service import get_search
class ResultView(TemplateView):
    template_name = "application/templates/search-result.html"

    def get_context_data(self, **kwargs):
        query = self.kwargs['query']
        list_bnb = get_search(query)
        context = super().get_context_data(**kwargs)
        context['list_bnb'] = list_bnb
        return context

