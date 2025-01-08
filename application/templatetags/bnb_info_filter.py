from django import template

from application.models import Account, BnbInformation
from application.models.accounts import Booking
from application.models.bnb import Review

register = template.Library()


@register.filter(name='current_user')
def current_user(user, session):
    return session.get('user') if session.get('user') is not None else None


@register.filter
def get_current_avatar(avatar_url, session):
    return Account.objects.filter(id=int(session.get('user'))).first().avatar if session.get(
        'user') is not None else None


@register.simple_tag(name='save_bnb_to_wishlists')
def save_bnb_to_wishlists(session, bnb_id):
    if session.get('user') is None or session.get('wishlists') is None: return None
    wishlist_session = session.get('wishlists')
    if bnb_id in wishlist_session: return wishlist_session
    wishlist_session.append(bnb_id)
    return wishlist_session


@register.simple_tag
def user_review_status(session, bnbid):
    if session.get('user') is None or bnbid is None: return False
    booking_data = Booking.objects.filter(account=Account.objects.filter(id=int(session.get('user'))).first(),
                                          bnb=BnbInformation.objects.filter(id=bnbid).first()).all()
    review_data = Review.objects.filter(account=Account.objects.filter(id=int(session.get('user'))).first(),
                                        bnb=BnbInformation.objects.filter(id=bnbid).first()).all()
    return len(booking_data) > len(review_data)
