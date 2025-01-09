from application.models.accounts import Account, WishList, WishListItems


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
        'avatar': user.avatar
        # 'wishlist': [bnb for bnb in WishList.objects.filter(account=user)]
    }

