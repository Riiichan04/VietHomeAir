from django.views.generic import TemplateView

class UserView(TemplateView):
    template_name = "application/templates/user.html" #default view

class UserInfoView(TemplateView):
    template_name = 'application/templates/user/user-information.html'