from django import template

from application.models import Account
from application.models.accounts import Booking
from application.models.bnb import Review

register = template.Library()


@register.filter(name='current_user')
def current_user(user, session):
    return session.user if session.get('user') is not None else None


@register.simple_tag
def user_review_status(session, bnb):
    if session.get('user') is None or bnb is None: return False
    booking_data = Booking.objects.filter(account=Account.objects.get(id=int(session.get('user'))), bnb=bnb).all()
    review_data = Review.objects.filter(account=Account.objects.get(id=int(session.get('user'))), bnb=bnb).all()
    return len(booking_data) > len(review_data)
