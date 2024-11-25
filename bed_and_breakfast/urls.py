from django.contrib import admin
from django.contrib import  admin
from django.urls import path, include

from application.views.LoginView import LoginView
from application.views.BasedView import BaseView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BaseView.as_view(), name=''),

    path('login/', LoginView.as_view(), name='login'),
]