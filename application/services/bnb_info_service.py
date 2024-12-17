from datetime import datetime
from math import trunc

from application.models import BnbInformation
from enum import Enum


# Lấy bnb còn active với id được chỉ định. Nếu không tìm thấy hoặc bnb có status = False sẽ trả về None
def get_bnb_info(bnb_id):
    bnb = BnbInformation.objects.filter(status=True).filter(id=bnb_id).first()
    if bnb is None: return None
    return {
        'name': bnb.name,
        'description': bnb.description,
        'images': [image.url for image in bnb.image_set.all()],
        'rules': [rule.description for rule in bnb.rule.all()],
        'services': ''.join(list(["- " + service.name + '\n' for service in bnb.service.all()])),
        'prices': calculate_price(bnb.price),
        'owner': bnb.owner.account,
        'categories': [category.name for category in bnb.category.all()],
        # Đánh giá của owner
        # Số lượng đánh giá của owner
        'reviews': [{'review_obj': review, 'display_content': display_review(review)} for review in bnb.review_set.all()],
        'sentiment_reviews': statistic_bnb_reviews_by_sentiment([review for review in bnb.review_set.all()]),
        'rating_reviews': statistic_bnb_reviews_by_rating([review for review in bnb.review_set.all()]),
    }


# Tính toán và hiển thị giá thuê bnb
def calculate_price(price, date=5, service_fee=70000):
    return {
        'default_price': '{0:,}'.format(price).replace('.00', '').replace(',', '.'),
        'base_bnb_price': '{0:,}'.format(price * date).replace('.00', '').replace(',', '.'),
        'final_bnb_price': '{0:,}'.format(price * date + service_fee).replace('.00', '').replace(',', '.')
    }


# Viết sau
def get_owner_info():
    return None


# Thống kê review của bnb theo sentiment
def statistic_bnb_reviews_by_sentiment(bnb_reviews):
    pos_reviews = [review.content for review in bnb_reviews if review.sentiment == 'positive']
    neg_reviews = [review.content for review in bnb_reviews if review.sentiment == 'negative']
    return {
        'pos_reviews': {'amount': len(pos_reviews), 'reviews': pos_reviews},
        'neg_reviews': {'amount': len(neg_reviews), 'reviews': neg_reviews}
    }


# Thống kê review của bnb theo số sao đánh giá
def statistic_bnb_reviews_by_rating(bnb_reviews):
    avg_rating = sum(map(lambda x: x.rating, bnb_reviews)) / len(bnb_reviews)
    count_rating = []
    for i in range(1, 6):
        count_rating.append(len([review.rating for review in bnb_reviews if review.rating == i]))

    return {
        'avg_rating': round(avg_rating, 2),
        'count_rating': tuple(count_rating)
    }


# Hiển thị html element cho
def display_review(review):
    html_result = '<div>'
    rating = review.rating
    for i in range(rating):
        html_result += '<i class="comment-rating__star fa-solid fa-star"></i>'
    for i in range(rating, 5):
        html_result += '<i class="comment-rating__star fa-regular fa-star"></i>'
    html_result += f'<span class="ms-2 h6 fw-semibold">{display_time(review.created_at)}</span>'
    html_result += '</div>'
    return html_result

def display_time(time):
    format_time = '%Y-%m-%d %H:%M:%S.%f'
    time_sec = datetime.strptime(datetime.strftime(time, format_time), format_time).timestamp()
    now_sec = datetime.now().timestamp()
    second_diff = round((now_sec - time_sec), 0)
    if second_diff < 0: return ''
    if second_diff < 60: return 'Bây giờ'
    time_in_milisec = [60 * 60 * 24 * 365, 60 * 60 * 24 * 31, 60 * 60 * 24 * 7, 60 * 60 * 24, 60 * 60, 60]
    label = [" năm trước", "tháng trước", " tuần trước", " ngày trước", " giờ trước", " phút trước"]
    converted_time = list(map(lambda x: int(round(second_diff / x, 0)), time_in_milisec))
    value_index = converted_time.index(list(filter(lambda x: x > 0, converted_time))[0])
    return str(converted_time[value_index]) + label[value_index]

