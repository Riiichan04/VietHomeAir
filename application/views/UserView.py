from django.views.generic import TemplateView

from application.services.user_service import get_user_info, get_wish_list_items


class UserView(TemplateView):
    template_name = "application/templates/user.html"  #default view

    def get_context_data(self, **kwargs):
        userId = self.request.session.get('user')
        context = super().get_context_data(**kwargs)
        context['userinfo'] = get_user_info(int(userId))
        print("OMGOMGOMG")
        print(get_user_info(int(userId)))
        return context

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