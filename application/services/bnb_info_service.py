import copy
from datetime import datetime, timedelta
import random

import requests
from django.db.models import Q

from application.models import BnbInformation
from application.models.accounts import Booking, OwnerReview, Account
from application.models.bnb import Review, ReviewClassification
from application.services.home_service import get_bnb_display_element


# Lấy bnb còn active với id được chỉ định. Nếu không tìm thấy hoặc bnb có status = False sẽ trả về None
def get_bnb_info(bnb_id):
    bnb = BnbInformation.objects.filter(status=True).filter(id=bnb_id).first()
    if bnb is None: return None
    booking_info = get_booking_date_range(get_booking_available_dates(bnb.id))
    return {
        'id': bnb.id,
        'name': bnb.name,
        'description': bnb.description,
        'images': [image.url for image in bnb.image_set.all()],
        'rules': rules_classify(bnb.rule),
        'services': ''.join(list(["- " + service.name + '\n' for service in bnb.service.all()])),
        'prices': calculate_price(bnb.price, booking_info[0]['range_length']),
        'owner': bnb.owner.account,
        'owner_review': [review for review in OwnerReview.objects.filter(owner=bnb.owner).all()],
        'location': bnb.location,
        # Sửa sau
        'owner_general_review': {'title': ' một chủ nhà rất xịn xò đó!',
                                 'description': 'Được mọi người đánh giá cao về chất lượng dịch vụ, là điểm đến lý tưởng của nhiều người'},
        'categories': [category.name for category in bnb.category.all()],
        'capacity': bnb.capacity,
        'booking': booking_info,
        # Đánh giá của owner
        # Số lượng đánh giá của owner
        'reviews': [{'review_obj': review, 'display_content': display_review(review)} for review in
                    bnb.review_set.all()],
        'sentiment_reviews': statistic_bnb_reviews_by_sentiment([review for review in bnb.review_set.all()]),
        'rating_reviews': statistic_bnb_reviews_by_rating([review for review in bnb.review_set.all()]),
    }


# Lấy các bnb tương tự (dựa vào category)


# Phân loại nội quy của nhà
def rules_classify(rules):
    labels = ['checkin', 'checkout', 'refund', 'secure', 'other']
    result = {}
    for label in labels:
        result[label] = [rule.description for rule in rules.filter(rule_type=label).all()]
    if len(result['other']) == 0: result['other'] = ['Nhà cho thuê này không còn nội quy nào khác']
    return result


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
    label = [" năm trước", " tháng trước", " tuần trước", " ngày trước", " giờ trước", " phút trước"]
    converted_time = list(map(lambda x: int(round(second_diff / x, 0)), time_in_milisec))
    value_index = converted_time.index(list(filter(lambda x: x > 0, converted_time))[0])
    return str(converted_time[value_index]) + label[value_index]


# Tìm những khoảng ngày có thể booking được
def get_booking_date_range(list_available_date):
    start_date = list_available_date[0]
    iterate_date = start_date['date']
    result = []  # Kết quả là một mảng chứa các range_obj
    range_obj = {  # Chứa ngày bắt đầu, ngày kết thúc và capacity
        'check_in': iterate_date.isoformat(),
        'check_out': iterate_date.isoformat(),
        'capacity': start_date['available_capacity'],
        'range_length': 1
    }
    flag = False
    for index in range(1, len(list_available_date)):
        iterate_date += timedelta(days=1)

        if iterate_date > list_available_date[index]['date']:
            return None  # Lỗi

        if iterate_date == list_available_date[index]['date']:  # Cập nhật lại ngày checkout và lấy min capacity
            if flag:
                range_obj['check_in'] = iterate_date.isoformat()
                range_obj['range_length'] = 1
                flag = False
            range_obj['check_out'] = iterate_date.isoformat()
            range_obj['capacity'] = min(range_obj['capacity'], list_available_date[index]['available_capacity'])
            range_obj['range_length'] += 1
            # Thêm một phần xử lý để hiển thị mặc định
            if index == 4 and len(result) == 0:
                default_obj = copy.deepcopy(range_obj)
                result.append(default_obj)
        if iterate_date < list_available_date[index]['date']:  # Nếu như ngày không hợp lệ chốt range_obj
            flag = True  # Flag = True để reset lại range_obj
            result.append(range_obj)

    result.append(range_obj)  # Thêm range_obj của index -1 vào
    return result


# Tìm ngày có thể đặt phòng tính từ hôm nay
def get_booking_available_dates(bnb_id):
    bnb = BnbInformation.objects.get(id=bnb_id)
    list_booked = Booking.objects.filter(bnb=bnb).all()

    # Tạm dùng vét cạn cho 1 tháng (khoảng 60 ngày) gần nhất
    now_date = datetime.now().date()
    target_date = now_date + timedelta(days=60)
    list_available_dates = []
    while now_date <= target_date:
        booking_result = is_booking_date_available(bnb, now_date)
        if booking_result['status']:
            list_available_dates.append({
                'date': now_date,
                'available_capacity': booking_result['available_capacity'],
            })
        now_date += timedelta(days=1)
    return list_available_dates


# Kiểm tra 1 ngày có thể đặt phòng không (Đang dùng phương pháp vét cạn)
def is_booking_date_available(bnb, date=datetime.now().date()):
    # Lấy ra tất cả booking mà có trạng thái không phải bị từ chối theo bnb đã truyền vào
    list_booked = Booking.objects.filter(bnb=bnb).filter(~Q(status='decline')).filter(~Q(status='served')).all()
    # Kiểm tra xem có booking nào đang được đặt không
    current_booking = [booking for booking in list_booked if booking.from_date.date() <= date <= booking.to_date.date()]

    if len(current_booking) == 0:  # Ngày này chưa có ai đặt
        return {
            'status': True,  # Nếu đã có người đặt thì kiểm tra xem còn chứa được ai không
            'available_capacity': bnb.capacity  # Còn lại bao nhiêu chỗ
        }

    current_capacity = sum([booking.capacity for booking in current_booking])
    return {
        'status': current_capacity < bnb.capacity,  # Nếu đã có người đặt thì kiểm tra xem còn chứa được ai không
        'available_capacity': bnb.capacity - current_capacity  # Còn lại bao nhiêu chỗ
    }
    # Quy định cách cách nào thực hiện ???
    # else: return {
    #     'status': False,  # Nếu đã có người đặt thì kiểm tra xem còn chứa được ai không
    #     'available_capacity': 0  # Còn lại bao nhiêu chỗ
    # }


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


# Dùng cho phần kiểm duyệt bình luận
def validate_review(review):
    input_review = {'sentence': review['content'], 'sentiment': 'None'}
    validate_result = requests.post('http://localhost:3110/review-validate/', json=input_review)
    if validate_result.status_code == 200:
        if validate_result.json()['result']:
            # Gọi hàm insert review vào bảng
            new_review = Review(bnb=BnbInformation.objects.filter(id=review['bnbId']).first(),
                                account=Account.objects.filter(id=review['accountId']).first(),
                                content=review['content'],
                                sentiment=validate_result.json()['content']['label'],
                                rating=int(review['rating']))
            new_review.save()
        else:
            # Insert vào spam review
            new_review = Review(bnb=BnbInformation.objects.filter(id=review['bnbId']).first(),
                                account=Account.objects.filter(id=review['accountId']).first(),
                                content=review['content'],
                                sentiment='none',
                                rating=int(review['rating']))
            spam_review = ReviewClassification(review=new_review, spam_status=True)
            new_review.save()
            spam_review.save()
        return True
    if validate_result.status_code == 400:
        return False


# Lấy các bnb tương tự
def get_similar_bnb(bnb_id):
    list_category = BnbInformation.objects.filter(status=True).filter(id=bnb_id).first().category.all()
    list_similar_bnb = BnbInformation.objects.filter(status=True).filter(category__in=list_category).exclude(id=bnb_id).distinct()
    list_similar_bnb_id = random.sample([bnb.id for bnb in list_similar_bnb],
                                        5 if list_similar_bnb.count() >= 5 else list_similar_bnb.count()) if list_similar_bnb else []
    return [get_bnb_display_element(similar_id) for similar_id in list_similar_bnb_id]
