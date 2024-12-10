from django.views.generic import TemplateView

class AboutUsView(TemplateView):
    template_name = 'application/templates/other_template/about-us.html'