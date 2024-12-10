from django.views.generic import TemplateView

class ResultView(TemplateView):
    template_name = "application/templates/search-result.html"