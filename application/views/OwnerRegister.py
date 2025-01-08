from django.views.generic import  TemplateView
from django.shortcuts import render

class OwnerRegisterView(TemplateView):
    template_name = 'application/templates/OwnerRegister.html'



