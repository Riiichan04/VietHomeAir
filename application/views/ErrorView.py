from django.shortcuts import render

def error_404(request, exception):
    return render(request, 'application/templates/error-404.html', {}, status=404)
