from application.models import BnbInformation
from application.models.bnb import Category, Image


# Lấy bnb còn active với id được chỉ định. Nếu không tìm thấy hoặc bnb có status = False sẽ trả về None
def get_bnb(bnb_id):
    return BnbInformation.objects.filter(status=True).filter(id=bnb_id).first()

# Kiểm tra bnb có khả dụng không
def is_bnb_valid(bnb_id):
    bnb = get_bnb(bnb_id)
    return bnb is not None


# Lấy tất cả category của bnb
def get_categories(bnb_id):
    return get_bnb(bnb_id).category.all() if is_bnb_valid(bnb_id) else None


# Lấy tất cả rule của bnb
def get_rules(bnb_id):
    return get_bnb(bnb_id).rule.all() if is_bnb_valid(bnb_id) else None


# Lấy tất cả service của bnb
def get_services(bnb_id):
    return get_bnb(bnb_id).service.all() if is_bnb_valid(bnb_id) else None


# Lấy thông tin chủ bnb của bnb
def get_owner(bnb_id):
    return get_bnb(bnb_id).owner if is_bnb_valid(bnb_id) else None


# Lấy thông tin hình ảnh của bnb thông qua truy xuất ngược
def get_bnb_images(bnb_id):
    return get_bnb(bnb_id).image_set.all() if is_bnb_valid(bnb_id) else None


# Lấy bình luận của bnb thông qua truy xuất ngược
def get_bnb_review(bnb_id):
    return get_bnb(bnb_id).review_set.all() if is_bnb_valid(bnb_id) else None


def get_full_bnb_info(bnb_id):
    return {
        "bnb_info": get_bnb(bnb_id),
        "categories": get_categories(bnb_id),
        "images": get_bnb_images(bnb_id),
        "owner": get_owner(bnb_id),
        "rules": get_rules(bnb_id),
        "services": get_services(bnb_id),
        "reviews": get_bnb_review(bnb_id),
    }
