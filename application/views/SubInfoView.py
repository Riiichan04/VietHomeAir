from django.views.generic import TemplateView
from django.http import HttpResponse

class PolicyViews(TemplateView):
    template_name = 'other_template/base.html'  #Default value

class ContactViews(TemplateView):
    template_name = 'other_template/about-us.html'