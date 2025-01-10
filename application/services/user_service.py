from django.http import Http404, JsonResponse

from application.models.accounts import Account, WishList, WishListItems
from application.services.home_service import get_bnb_display_element


def get_user_info(user_id):
    user = Account.objects.filter(status=True).filter(id=user_id).first()
    if user is None: return None
    return {
        'id': user.id,
        'username': user.username,
        'password': user.password,
        'email': user.email,
        'phone': user.phone,
        'description': user.description,
        'fullname': user.fullname,
        'gender': user.gender,
        'is_verified': user.is_verified,
        'avatar': user.avatar,
    }


# @login_required
# def update_user_info(request):
#     if request.method == 'POST':
#         userId= request.session.get('user')
#         user= Account.objects.filter(id=userId).first()
#         user.username= request.POST.get('username')
#         user.email= request.POST.get('email')
#         user.phone= request.POST.get('phone')
#         user.save()
#         return JsonResponse({'message': 'User updated successfully!'})
def get_wish_list(user_id: int):
    user = Account.objects.filter(id=user_id).first()
    if user is None: return None
    wishlist = WishList.objects.filter(account=user).first()
    if wishlist is None: raise Http404("Hong có WishList")
    return wishlist


def get_wish_list_items(user_id: int):
    wishlist = get_wish_list(user_id)
    if wishlist is None: return None
    wishlist_items_id = WishListItems.objects.filter(wishlist=wishlist)
    if wishlist_items_id is None: return []
    return [get_bnb_display_element(bnb_id) for bnb_id in wishlist_items_id]
