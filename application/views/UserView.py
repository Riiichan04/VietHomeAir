from django.views.generic import TemplateView


class UserView(TemplateView):
    template_name = "application/templates/user.html"  #default view


class UserInfoView(TemplateView):
    template_name = 'application/templates/user/user-information.html'


class UserOrderHistoryView(TemplateView):
    template_name = 'application/templates/user/user-order-history.html'


class UserViewedHistoryView(TemplateView):
    template_name = 'application/templates/user/user-viewed-history.html'


class UserReviewHistoryView(TemplateView):
    template_name = 'application/templates/user/user-reviewed-history.html'

class UserWishListView(TemplateView):
    template_name = 'application/templates/user/user-wishlist.html'
