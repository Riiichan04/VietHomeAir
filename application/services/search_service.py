from application.models import BnbInformation
from application.services.home_service import get_bnb_display_element


# Hiển thị thông tin bnb
def get_bnb_result_info(bnb_id):
    return get_bnb_display_element(bnb_id)
# Lấy bnb theo kết quả tìm kiếm
def get_bnb_result(searchkey):
    query="""
        SELECT bnb.id
        FROM application_bnbinformation as bnb
        WHERE bnb.status = TRUE
        AND (bnb.name LIKE ?)
        LIMIT 5
    """
    list_id= [bnb.id for bnb in BnbInformation.objects.raw(query, ['%' + searchkey + '%', True])]
    print(list_id)
    return [bnb.id for bnb in BnbInformation.objects.filter(id__in=list_id).all()]
