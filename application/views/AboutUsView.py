from django.views.generic import TemplateView

class AboutUsView(TemplateView):
    template_name = 'application/templates/about-us.html'