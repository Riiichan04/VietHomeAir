from application.models import BnbInformation

# Lấy bnb còn active với id được chỉ định. Nếu không tìm thấy hoặc bnb có status = False sẽ trả về None
def get_bnb(bnb_id):
    return BnbInformation.objects.filter(status=True).filter(id=bnb_id).first()
