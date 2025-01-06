from django.http import Http404
from django.views.generic import TemplateView

from application.services.category_service import get_category, get_bnb_by_category, get_category_original_name


class CategoryView(TemplateView):
    template_name = "application/templates/category.html"

    def get_context_data(self, **kwargs):
        category_name = self.kwargs['category_name']
        category = get_category(category_name)
        if category is None: raise Http404("Tìm cái j thế?")
        list_bnb_data = get_bnb_by_category(category_name)
        context = super().get_context_data(**kwargs)
        context['category_name'] = get_category_original_name(category)
        context['list_bnb_data'] = list_bnb_data
        return context