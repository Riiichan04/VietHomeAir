from django import template

from application.models.accounts import Booking
from application.models.bnb import Review

register = template.Library()

@register.filter(name='current_user')
def current_user(user, session):
    return session.user if session.get('user') is not None else None

@register.filter(name='is_user_can_comment')
def is_user_can_comment(user, param_obj):
    if param_obj['user'] or param_obj['bnb'] is None: return False
    booking_data = Booking.objects.filter(account=int(param_obj['user']), bnb=param_obj['bnb']).all()
    review_data = Review.objects.filter(account=int(param_obj['user']), bnb=param_obj['bnb']).all()
    return len(booking_data) > len(review_data)