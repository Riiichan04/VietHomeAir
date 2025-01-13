import os
import smtplib
from datetime import timezone
from math import trunc
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.termcolors import foreground
from django.utils.timezone import now
from django.views.generic import TemplateView
from django.contrib import messages
from application.models import Account
from application.services.auth_service import user_login, validate_new_user
from application.views.ErrorView import context


class LoginView(TemplateView):
    template_name = 'application/templates/auth_template/login.html'

class RegisterView(TemplateView):
    template_name = 'application/templates/auth_template/register.html'

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

        # elif form_type == 'register':
        #     if request.method == 'POST':
        #         # Lấy dữ liệu từ request
        #         username = request.POST.get('username')
        #         email = request.POST.get('email')
        #         fullname = request.POST.get('fullname')
        #         password = request.POST.get('password')
        #         repassword = request.POST.get('repassword')
        #         gender = request.POST.get('gender')
        #         phone = request.POST.get('phone')
        #
        #         print(f"Username: {username}, Email: {email}, Fullname: {fullname}, Password: {password}, Repassword: {repassword}, Gender: {gender}, Phone: {phone}")
        #
        #         if Account.objects.filter(username=username).exists():
        #             return JsonResponse({'result': False, 'message': 'Tên người dùng đã tồn tại'}, status=400)
        #
        #         if Account.objects.filter(email=email).exists():
        #             return JsonResponse({'result': False, 'message': 'Email đã tồn tại'}, status=400)
        #
        #         if password != repassword:
        #             return JsonResponse({'result': False, 'message': 'Passwords do not match'}, status=400)
        #
        #         account = Account.objects.create(
        #             username=username,
        #             password=make_password(password),
        #             email=email,
        #             phone=phone,
        #             fullname=fullname,
        #             gender=gender,
        #             role=0,
        #             registered_time=timezone.now(),
        #             is_verified=True,
        #             status=True
        #         )
        #         account.save()
        #
        #     return JsonResponse({'result': True, 'message': 'Đăng ký thành công'}, status=200)
        return JsonResponse({'result': False}, status=400)

class ForgetPasswordHandler(TemplateView):
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        account = Account.objects.filter(email=email).first()
        if account is None: return
        s = smtplib.SMTP('smtp.gmail.com', 587) #Tạo session
        s.starttls()    #Bảo mật
        s.login(os.getenv('MAIL_SENDER'), os.getenv('PASSWORD_SENDER'))
        message = f'Mật khẩu của bạn là {account.password}'
        s.sendmail(os.getenv('MAIL_SENDER'), email, message)
        s.quit()