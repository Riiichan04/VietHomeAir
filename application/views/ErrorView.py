from django.shortcuts import render
from django.views.generic import TemplateView

context = {
    'status_code': 404  # Mặc định hiển thị lỗi 404
}


def get_error_400_page(request, exception=None):
    return render(request, 'application/templates/error.html', context, status=400)


def get_error_403_page(request, exception=None):
    return render(request, 'application/templates/error.html', context, status=403)


def get_error_404_page(request, exception=None):
    return render(request, 'application/templates/error.html', context, status=404)


def get_error_500_page(request, exception=None):
    context["status_code"] = 500
    return render(request, 'application/templates/error.html', context, status=500)
