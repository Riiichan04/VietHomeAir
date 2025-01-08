# Lấy thông tin cơ bản để hiển thị bnb dựa trên
from application.models import BnbInformation


# Lấy thông tin hiển thị bnb
def get_bnb_display_element(bnb_id):
    bnb = BnbInformation.objects.filter(status=True).filter(id=bnb_id).first()
    if bnb is None: return None
    return {
        'id': bnb.id,
        'name': bnb.name,
        'description': bnb.description,  # Xử lý sau
        'thumbnail': bnb.image_set.first().url if bnb.image_set.first() is not None else '',
        'owner': bnb.owner.account.fullname,
        'avg_rating': str(calculate_avg_bnb_rating([review for review in bnb.review_set.all()]))
    }


# Tính toán rating trung bình của bnb
def calculate_avg_bnb_rating(bnb_reviews):
    return round(sum(map(lambda x: x.rating, bnb_reviews)) / len(bnb_reviews), 2)


# Lấy id của bnb có lượt xem cao nhất
def get_most_viewed_bnb():
    return [bnb.id for bnb in BnbInformation.objects.filter(status=True).order_by('count_viewed')[:5]]


# Lấy id của bnb có đánh giá cao nhất
def get_most_rated_bnb():
    query = """
        select id
        from application_bnbinformation as info join (
            select bnb_id, avg(rating) as avg_rating
            from application_review
            group by bnb_id
            order by avg_rating desc
        ) as review on info.id = review.bnb_id
        where info.status = True        
        limit 5
    """

    list_id = [bnb.id for bnb in BnbInformation.objects.raw(query)]
    return [bnb.id for bnb in BnbInformation.objects.filter(id__in=list_id).all()]
