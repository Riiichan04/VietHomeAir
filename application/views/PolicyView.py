from django.views.generic import TemplateView
from django.http import HttpResponse

class PolicyViews(TemplateView):
    template_name = 'policy/base.html'  #Default value

