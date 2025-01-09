from django.http import JsonResponse
from django.shortcuts import render
from  django.views.generic import TemplateView
from django.contrib.auth.hashers import make_password
from application.models import Account
from application.services.auth_service import validate_new_user


class RegisterView(TemplateView):
    template_name = 'application/templates/auth_template/register.html'

    def get_context_data(self,request, *args, **kwargs):
        # lay thong tin tu request
        email = request.POST.get('email')
        username = request.POST.get('username')
        full_name = request.POST.get('full_name')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        gender = request.POST.get('gender')


        # Ktra cac trương dữ liệu
        if not all([email, username, full_name, password, repassword, gender]):
            return JsonResponse({'result': False, 'message': 'Vui lòng nhập đủ thông tin'}, status=400)

        if password != repassword:
            return JsonResponse({'result': False, 'message': 'Mật khẩu và xác nhận mật khẩu không khớp'}, status=400)

        if not validate_new_user(username, email):
            return JsonResponse({'result': False, 'message': 'Tên người dùng hoặc email đã tồn tại'}, status= 400)

        # Tạo tài khoản mới
        try:
            new_user = Account.objects.create(username=username,
                                              email=email,
                                              full_name=full_name,
                                              password=make_password(password),
                                              gender=gender,
                                              )
            return  JsonResponse({'result': True, 'message': 'Đăng ký thành công'}, status=200)
        except Exception as e:
            return JsonResponse({'result': False, 'message': f'Lỗi hệ thống: {str(e)}'}, status=500)