from datetime import datetime, timedelta

from django.db.models import Q

from application.models import BnbInformation
from application.models.accounts import Booking


# Lấy bnb còn active với id được chỉ định. Nếu không tìm thấy hoặc bnb có status = False sẽ trả về None
def get_bnb_info(bnb_id):
    bnb = BnbInformation.objects.filter(status=True).filter(id=bnb_id).first()
    if bnb is None: return None
    return {
        'id': bnb.id,
        'name': bnb.name,
        'description': bnb.description,
        'images': [image.url for image in bnb.image_set.all()],
        'rules': [rule.description for rule in bnb.rule.all()],
        'services': ''.join(list(["- " + service.name + '\n' for service in bnb.service.all()])),
        'prices': calculate_price(bnb.price),
        'owner': bnb.owner.account,
        'categories': [category.name for category in bnb.category.all()],
        'capacity': bnb.capacity,
        # Đánh giá của owner
        # Số lượng đánh giá của owner
        'reviews': [{'review_obj': review, 'display_content': display_review(review)} for review in
                    bnb.review_set.all()],
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


# Thống kê review của bnb theo sentiment
def statistic_bnb_reviews_by_sentiment(bnb_reviews):
    pos_reviews = [review.content for review in bnb_reviews if review.sentiment == 'positive']
    neg_reviews = [review.content for review in bnb_reviews if review.sentiment == 'negative']
    return {
        'pos_reviews': {'amount': len(pos_reviews), 'reviews': pos_reviews},
        'neg_reviews': {'amount': len(neg_reviews), 'reviews': neg_reviews},
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


# Hiển thị thời gian bình luận
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


# Tìm ngày có thể đặt phòng tính từ hôm nay
def get_booking_available_dates(bnb_id):
    bnb = BnbInformation.objects.get(id=bnb_id)
    list_booked = Booking.objects.filter(bnb=bnb).all()
    # booking_checkin_date = [booking.from_date for booking in list_booked if
    #                         booking.from_date.date() >= datetime.now().date()]
    # booking_checkout_date = [booking.to_date for booking in list_booked if
    #                          booking.to_date.date() >= datetime.now().date()]

    # Tạm dùng vét cạn cho 1 tháng (khoảng 31 ngày) gần nhất
    now_date = datetime.now().date()
    target_date = now_date + timedelta(days=31)
    list_available_dates = []
    while now_date <= target_date:
        if is_booking_date_available(bnb, now_date):
            list_available_dates.append(now_date.strftime("%Y-%m-%d"))
        now_date += timedelta(days=1)
    return list_available_dates


# Kiểm tra 1 ngày có thể đặt phòng không (Đang dùng phương pháp vét cạn)
def is_booking_date_available(bnb, date=datetime.now().date()):
    # Lấy ra tất cả booking mà có trạng thái không phải bị từ chối theo bnb đã truyền vào
    list_booked = Booking.objects.filter(bnb=bnb).filter(~Q(status='decline')).all()
    # Kiểm tra xem có booking nào đang được đặt không
    current_booking = [booking for booking in list_booked if booking.from_date.date() <= date <= booking.to_date.date()]

    if len(current_booking) == 0:
        return True  # Ngày này có thể book được

    current_capacity = sum([booking.capacity for booking in current_booking])
    return current_capacity < bnb.capacity


# Dùng cho web filter
def statistic_review_by_id(bnb_id):
    reviews = [review for review in
               BnbInformation.objects.filter(status=True).filter(id=bnb_id).first().review_set.all()]
    pos_reviews = [review for review in reviews if review.sentiment == 'positive']
    neg_reviews = [review for review in reviews if review.sentiment == 'negative']
    return {
        'pos_reviews': {'amount': len(pos_reviews), 'reviews': pos_reviews},
        'neg_reviews': {'amount': len(neg_reviews), 'reviews': neg_reviews},
        'all_reviews': {'amount': len(reviews), 'reviews': [review for review in reviews]}
    }
