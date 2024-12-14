"""
URL configuration for bed_and_breakfast project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, re_path, include

from application.views.SubInfoView import PolicyViews, ContactViews
from application.views.ProductView import ProductView
from application.views.LoginView import AuthView
from application.views.HomeView import HomeView
from application.views.ResultView import ResultView
from application.views.BookView import BookView
from application.views.InfoOwnerView import InfoOwnerView

# Lưu ý: Nếu muốn hiển thị các trang lỗi custom thì phải set DEBUG = False và phải set ALLOWED_HOSTS
# (Trong môi trường dev thì hãy đặt ALLOWED_HOSTS = ["localhost"])
# Xem https://docs.djangoproject.com/en/5.1/ref/views/#django.views.defaults.page_not_found
# Xem định nghĩa default các public url ở .venv/Lib/django/conf/urls/__init__.py

handler400 = 'application.views.ErrorView.get_error_400_page'
handler403 = 'application.views.ErrorView.get_error_403_page'
handler404 = 'application.views.ErrorView.get_error_404_page'
handler500 = 'application.views.ErrorView.get_error_500_page'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name=''),
    path('product/', ProductView.as_view(), name='product'),
    path('privacy/', PolicyViews.as_view(template_name='other_template/privacy-policy.html'), name='privacy-policy'),
    path('terms-of-use/', PolicyViews.as_view(template_name='other_template/terms.html'), name='terms-of-use'),
    path('policy/', PolicyViews.as_view(template_name='other_template/other-policy.html'), name='terms-of-use'),
    re_path(r'^(login|register|forgot-password)/$', AuthView.as_view(), name='auth'),
    path('about-us/', ContactViews.as_view(template_name='other_template/about-us.html'), name='about-us'),
    path('contact/', ContactViews.as_view(template_name='other_template/contact-us.html'), name='contact-us'),
    path('result/', ResultView.as_view(), name='result'),
    path('book/', BookView.as_view(), name='book'),
    path('info-owner/', InfoOwnerView.as_view(), name='info-owner'),
]
