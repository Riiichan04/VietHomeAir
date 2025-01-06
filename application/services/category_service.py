from application.models import BnbInformation
from application.models.bnb import Category
from application.services.home_service import get_bnb_display_element
import unicodedata

vietnamese_characters = str.maketrans(
    "ÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬĐÈÉẺẼẸÊẾỀỂỄỆÍÌỈĨỊÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÚÙỦŨỤƯỨỪỬỮỰÝỲỶỸỴáàảãạăắằẳẵặâấầẩẫậđèéẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵ",
    "A" * 17 + "D" + "E" * 11 + "I" * 5 + "O" * 17 + "U" * 11 + "Y" * 5 + "a" * 17 + "d" + "e" * 11 + "i" * 5 + "o" * 17 + "u" * 11 + "y" * 5
)

def get_category(category_name: str):
    category_filter_result = [category for category in Category.objects.all() if
                              remove_vietnamese_characters(category.name).replace(' ', '').lower() ==
                              remove_vietnamese_characters(category_name).replace(' ', '').lower()]
    return category_filter_result[0] if category_filter_result != [] else None

def get_category_original_name(category):
    return category.name

def get_bnb_by_category(category_name):
    category = get_category(category_name)
    if category is None: return None
    return [get_bnb_display_element(bnb.id) for bnb in BnbInformation.objects.filter(category=category)]


def remove_vietnamese_characters(txt: str):
    if not unicodedata.is_normalized("NFC", txt):
        txt = unicodedata.normalize("NFC", txt)
    return txt.translate(vietnamese_characters)
