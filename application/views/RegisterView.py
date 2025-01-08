from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from django.views import View
from application.models import Account
from django.utils.timezone import now

class RegisterView(View):
    def get(self, request, type):
        if type == 'register':
            return render(request, 'auth_template/register.html')
        return render(request, 'auth_template/login.html')  # Mặc định là trang login

    def post(self, request, type):
        if type == 'register':
            username = request.POST.get('username', '').strip()
            email = request.POST.get('email', '').strip()
            fullname = request.POST.get('fullname', '').strip()
            password = request.POST.get('password', '').strip()
            repassword = request.POST.get('repassword', '').strip()
            gender = request.POST.get('gender', '').strip()
            phone = request.POST.get('phone', '').strip()

            # Kiểm tra các trường bắt buộc
            if not all([username, email, fullname, password, repassword, gender]):
                return JsonResponse({'result': False, 'message': 'Vui lòng điền đầy đủ thông tin.'}, status=400)

            # Kiểm tra tên người dùng hoặc email trùng lặp
            if Account.objects.filter(username=username).exists():
                return JsonResponse({'result': False, 'message': 'Tên đăng nhập đã tồn tại.'}, status=400)
            if Account.objects.filter(email=email).exists():
                return JsonResponse({'result': False, 'message': 'Email đã tồn tại.'}, status=400)

            # Kiểm tra mật khẩu
            if password != repassword:
                return JsonResponse({'result': False, 'message': 'Mật khẩu không khớp.'}, status=400)

            # Tạo tài khoản mới
            try:
                account = Account.objects.create(
                    username=username,
                    password=password,
                    email=email,
                    phone=phone,
                    fullname=fullname,
                    gender=gender,
                    role=0,
                    is_verified=True,
                    status=True
                )
                account.save()
                return JsonResponse({'result': True, 'message': 'Đăng ký thành công!'}, status=200)
            except Exception as e:
                return JsonResponse({'result': False, 'message': f'Có lỗi xảy ra: {e}'}, status=500)

        return JsonResponse({'result': False, 'message': 'Yêu cầu không hợp lệ.'}, status=400)
