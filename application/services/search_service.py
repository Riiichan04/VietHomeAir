from application.services.home_service import get_bnb_display_element
from application.models.bnb import BnbInformation
import unicodedata


vietnamese_characters= str.maketrans("ÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬĐÈÉẺẼẸÊẾỀỂỄỆÍÌỈĨỊÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÚÙỦŨỤƯỨỪỬỮỰÝỲỶỸỴáàảãạăắằẳẵặâấầẩẫậđèéẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵ",
    "A" * 17 + "D" + "E" * 11 + "I" * 5 + "O" * 17 + "U" * 11 + "Y" * 5 + "a" * 17 + "d" + "e" * 11 + "i" * 5 + "o" * 17 + "u" * 11 + "y" * 5)

def get_search(query:str):
    search_results= [bnb for bnb in BnbInformation.objects.all()
                     if remove_vietnamese_characters(bnb.name).replace(' ','').lower().__contains__(remove_vietnamese_characters(query).replace(' ','').lower())]
    return search_results[0] if search_results!=[] else None


def get_bnb_by_result(query):
    searchKey= get_search(query)
    if searchKey is None: return None
    return [get_bnb_display_element(bnb.id) for bnb in BnbInformation.objects.filter(name__icontains=searchKey)] #ham rong

def remove_vietnamese_characters(query:str):
    if not unicodedata.is_normalized("NFC",query):
        query= unicodedata.normalize("NFC",query)
    return query.translate(vietnamese_characters)