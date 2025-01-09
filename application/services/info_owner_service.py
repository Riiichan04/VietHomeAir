from django.db.models import Avg

from application.models import Owner
from application.models.accounts import OwnerReview
from application.models.bnb import Review, BnbInformation


def get_info_owner(owner_id):
    owner = Owner.objects.filter(id=owner_id).first()
    if owner is None:
        return None
    # Đếm số lượng đánh giá
    review_count = get_bnb_reviews(owner.id).count()
    # Filter reviews for the specific owner and compute the average rating
    avg_rating = get_bnb_reviews(owner.id).aggregate(Avg('rating'))
    avg_rating = '' if avg_rating['rating__avg'] is None else round(avg_rating['rating__avg'], 2)
    return {
        'id': owner.id,
        'username': owner.account.username,
        'fullname': owner.account.fullname,
        'avatar': owner.account.avatar,
        'email': owner.account.email,
        'phone': owner.account.phone,
        'rating': avg_rating,
        'review_count': review_count,
        'description': owner.account.description,
        'is_verified': owner.account.is_verified,
    }

def get_bnb_reviews(owner_id):
    return Review.objects.filter(bnb__owner__id=owner_id)

# lấy thông tin bnb của chủ nhà
def get_list_info_bnb_avg_rating(owner_id):
    list_bnb = BnbInformation.objects.filter(status=True).select_related('owner').filter(owner__id=owner_id)
    if not list_bnb.exists():  # Kiểm tra nếu QuerySet rỗng
        return []
    result = []
    for bnb in list_bnb:
        result.append({
            "id": bnb.id,  # Chỉ lấy id
            "name": bnb.name,  # Chỉ lấy tên
            "url": bnb.image_set.all()[0].url,
            "owner_name": bnb.owner.account.fullname,
            "description": bnb.description,  # Lấy giá
            "avg_rating": get_avg_rating_bnb(bnb.id)  # Đánh giá trung bình
        })
    return result

def get_avg_rating_bnb(bnb_id):
    avg_rating = Review.objects.select_related('bnb').filter(bnb__id=bnb_id).aggregate(Avg('rating'))
    avg_rating = '' if avg_rating is None else round(avg_rating['rating__avg'], 2)
    return avg_rating