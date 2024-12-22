from django.views.generic import TemplateView
from django.http import HttpResponse

class OwnerManagementView(TemplateView):
    template_name = 'manage_of_owner/base.html'