from django import template

register = template.Library()

@register.filter(name='filter_review_by_sentiment')
def filter_review_by_sentiment(reviews, sentiment):
    if sentiment == 'positive':
        return [review.content for review in reviews if review.sentiment == 'positive']
    if sentiment == 'negative':
        return [review.content for review in reviews if review.sentiment == 'negative']