from django.views.generic import TemplateView

class ContactView(TemplateView):
    template_name = "application/templates/other_template/contact-us.html"