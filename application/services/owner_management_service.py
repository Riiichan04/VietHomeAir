import locale

from application.models import Account, BnbInformation
from application.models.accounts import Owner, OwnerReview
from application.models.bnb import Category, Service, Rule


#lấy thông tin hiển thị thông tin chủ nhà
def get_info_owner(user_id):
    owner = Owner.objects.select_related('account').get(account__id=user_id)
    if owner is None: return None
    # Đếm số lượng đánh giá
    review_count = OwnerReview.objects.filter(owner=owner).count()
    return {
        'id': owner.id,
        'username': owner.account.username,
        'fullname': owner.account.fullname,
        'avatar': owner.account.avatar,
        'email': owner.account.email,
        'phone': owner.account.phone,
        'rating': owner.rating,
        'review_count': review_count,
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
