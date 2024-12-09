from django.shortcuts import render
from django.views.generic import TemplateView

class LoginView(TemplateView):
    template_name = 'application/templates/auth_template/login.html'

class AuthView(TemplateView):
    template_name = 'application/templates/auth_template/base.html'

    # def get(self, request, *args, **kwargs):
    #     # Gọi các form
    #     login_form = None
    #     register_form = None
    #     forget_password_form = None
    #     active_form = None
    #
    #     # Lấy form đang được chọn
    #     form_type = self.kwargs.get('form_type')
    #
    #     # Truyền form vào
    #     if form_type == 'login':
    #         active_form = login_form
    #     elif form_type == 'register':
    #         active_form = register_form
    #     elif form_type == 'forget_password':
    #         active_form = forget_password_form
    #
    #     return render(request, 'auth_template/login.html', {'active_form': active_form})
    #
    # def post(self, request, *args, **kwargs):
    #     return None