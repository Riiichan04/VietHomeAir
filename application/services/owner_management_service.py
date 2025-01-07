import locale

from django.db.models import Avg

from application.models import Account, BnbInformation
from application.models.accounts import Owner, OwnerReview
from application.models.bnb import Category, Service, Rule, Review


#lấy thông tin hiển thị thông tin chủ nhà
def get_info_owner(user_id):
    owner = Owner.objects.select_related('account').get(account__id=user_id)
    if owner is None: return None
    # Đếm số lượng đánh giá
    review_count = OwnerReview.objects.filter(owner=owner).count()
    # Filter reviews for the specific owner and compute the average rating
    avg_rating = OwnerReview.objects.filter(owner=owner).aggregate(Avg('rating'))
    avg_rating = '' if avg_rating is None else round(avg_rating['rating__avg'], 2)
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

#lấy thông tin bnb của chủ nhà
def get_list_info_bnb(owner_id):
    list_bnb = BnbInformation.objects.select_related('owner').filter(owner__id=owner_id)
    if not list_bnb.exists():  # Kiểm tra nếu QuerySet rỗng
        return []
    # Định dạng giá cho mỗi BnB
    locale.setlocale(locale.LC_ALL, 'vi_VN.UTF-8')  # Đặt locale cho Việt Nam
    for bnb in list_bnb:
    # Định dạng giá của BnB (ví dụ: 1,000,000 VND)
        bnb.price = locale.format_string("%d", bnb.price, grouping=True)
    return list_bnb

def get_bnb_by_id(bnb_id):
    bnb = BnbInformation.objects.filter(status=True).filter(id=bnb_id).first()
    if bnb is None: return None
    return {
        'id': bnb.id,
        'name': bnb.name,
        'description': bnb.description,
        'images': [image for image in bnb.image_set.all()],
        'rules': bnb.rule.all(),
        'services': bnb.service.all(),
        'prices': bnb.price,
        'location': bnb.location,
        'categories': bnb.category.all(),
        'capacity': bnb.capacity,
    }

def get_owner_reviews(owner_id):
    owner_reviews = OwnerReview.objects.select_related('owner').filter(owner__id=owner_id).all()
    if not owner_reviews: return []
    return owner_reviews

def get_list_category():
    categories = Category.objects.all()
    return categories

def get_list_service():
    services = Service.objects.all()
    return services

def get_list_rule():
    rules = Rule.objects.all()
    return rules

def get_bnb(bnb_id):
    bnb = BnbInformation.objects.filter(id=bnb_id).first()
    if bnb is None: return None
    return bnb

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
