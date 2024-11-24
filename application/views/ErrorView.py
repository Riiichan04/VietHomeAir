from django.shortcuts import render

context = {
    'status_code': 404  # Mặc định hiển thị lỗi 404
}


def error_400(request, exception=None):
    return render(request, 'application/templates/error.html', exception, context, status=400)

def error_403(request, exception=None):
    return render(request, 'application/templates/error.html', exception, context, status=403)

def error_404(request, exception):
    return render(request, 'application/templates/error.html', context, status=404)

def error_500(request, exception=None):
    context["status_code"] = 500
    return render(request, 'application/templates/error.html', exception, context, status=500)