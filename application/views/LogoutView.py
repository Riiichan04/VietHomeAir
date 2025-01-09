from django.shortcuts import redirect


def logout_view(request):
    # Xóa toàn bộ session của user
    request.session.flush()
    return redirect('/login')