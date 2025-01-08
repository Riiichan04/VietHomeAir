from django import template

from application.models import BnbInformation

register = template.Library()

@register.filter(name='get_images_by_bnbid')
def get_images_by_bnbid(list_image, bnbid):
    return [image.url for image in BnbInformation.objects.filter(status=True).filter(id=bnbid).first().image_set.all()]