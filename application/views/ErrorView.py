from django.shortcuts import render


def error_400(request, exception=None):
    return render(request, 'application/templates/error-404.html', exception, {}, status=400)


def error_403(request, exception=None):
    return render(request, 'application/templates/error-404.html', exception, {}, status=403)


def error_404(request, exception):
    return render(request, 'application/templates/error-404.html', {}, status=404)


def error_500(request, exception=None):
    return render(request, 'application/templates/error-404.html', exception, {}, status=500)
