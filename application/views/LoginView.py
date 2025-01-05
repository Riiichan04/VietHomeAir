from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.hashers import check_password
from application.models import accounts

from application.services.auth_service import user_login


class LoginView(TemplateView):
    template_name = 'application/templates/auth_template/login.html'


class AuthView(TemplateView):
    template_name = 'application/templates/auth_template/base.html'

    def post(self, request, *args, **kwargs):
        form_type = self.kwargs['type']
        # if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if form_type == 'login':
            auth_user = user_login(request.POST.get('username'), request.POST.get('password'))
            if auth_user is not None:
                request.session['user'] = auth_user['id']
                return JsonResponse({'result': True}, status=200)
            else:
                return JsonResponse({'result': False}, status=200)
        else:
            return JsonResponse({'result': False}, status=404)
