import json

from django.http import JsonResponse
from django.views.generic import TemplateView

from application.models.accounts import Account
from application.services.user_service import get_user_info, get_wish_list_items


class UserView(TemplateView):
    template_name = "application/templates/user.html"  #default view

    def get_context_data(self, **kwargs):
        userId = self.request.session.get('user')
        context = super().get_context_data(**kwargs)
        context['userinfo'] = get_user_info(int(userId))
        return context

class UpdateUserView(TemplateView):
    def post(self, request, *args, **kwargs):
            # Xử lý dữ liệu từ request.POST
        userId = self.request.session.get('user')
        user= Account.objects.filter(status=True).filter(id=userId).first()
        data = json.loads(request.body)
        username = data.get('username')
        email = data.get('email')
        phone = data.get('phone')

        user.username=username
        user.email=email
        user.phone=phone
        user.save()
        return JsonResponse({'message': 'User information updated successfully!'})

    def get(self, request, *args, **kwargs):
        return JsonResponse({"message": "GET method not allowed"}, status=405)

class UserInfoView(TemplateView):
    template_name = 'application/templates/user/user-information.html'
    def get_context_data(self, **kwargs):
        userId = self.request.session.get('user')
        context = super().get_context_data(**kwargs)
        context['userinfo'] = get_user_info(int(userId))
        return context

class UserOrderHistoryView(TemplateView):
    template_name = 'application/templates/user/user-order-history.html'


class UserViewedHistoryView(TemplateView):
    template_name = 'application/templates/user/user-viewed-history.html'


class UserReviewHistoryView(TemplateView):
    template_name = 'application/templates/user/user-reviewed-history.html'

class UserWishListView(TemplateView):
    template_name = 'application/templates/user/user-wishlist.html'

    def get_context_data(self, **kwargs):
        userId = self.request.session.get('user')
        print(userId)
        context = super().get_context_data(**kwargs)
        context['wishlist']= get_wish_list_items(int(userId))
        return context