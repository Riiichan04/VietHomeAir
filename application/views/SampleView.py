from django.views.generic import TemplateView

class HelloViews(TemplateView):
    template_name = "application/templates/base.html"
