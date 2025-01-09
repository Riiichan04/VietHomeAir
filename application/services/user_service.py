from django.http import Http404

from application.models.accounts import Account, WishList, WishListItems
from application.services.home_service import get_bnb_display_element

def get_user_info(user_id):
    user= Account.objects.filter(status=True).filter(id=user_id).first()
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

def get_wish_list(user_id:int):
    user= Account.objects.filter(id=user_id).first()
    if user is None: return None
    wishlist = WishList.objects.filter(account=user).first()
    if wishlist is None: raise Http404("Hong có WishList")
    return wishlist

def get_wish_list_items(user_id:int):
    wishlist = get_wish_list(user_id)
    if wishlist is None: return None
    wishlist_items_id= WishListItems.objects.filter(wishlist=wishlist)
    if wishlist_items_id is None: return []
    return [get_bnb_display_element(bnb_id) for bnb_id in wishlist_items_id]
