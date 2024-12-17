# Lấy thông tin cơ bản để hiển thị bnb dựa trên
from application.models import BnbInformation


def get_bnb_display_element(bnb_id):
    bnb = BnbInformation.objects.filter(status=True).filter(id=bnb_id).first()
    if bnb is None: return None
    return {
        'name': bnb.name,
        'description': bnb.description,  # Xử lý sau
        'thumbnail': bnb.image_set.first().url,
        'owner': bnb.owner.account,
        'avg_rating': str(calculate_avg_bnb_rating([review for review in bnb.review_set.all()]))
    }


def calculate_avg_bnb_rating(bnb_reviews):
    return sum(map(lambda x: x.rating, bnb_reviews)) / len(bnb_reviews)
