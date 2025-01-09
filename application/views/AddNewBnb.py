from itertools import product

from cloudinary.uploader import upload
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.shortcuts import render

from application.models import BnbInformation
from application.models.bnb import Service, Rule, Category, Location, Image


class AddNewBnb(TemplateView):
    template_name = 'application/templates/create-new-bnb.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_services'] = [service.name for service in Service.objects.all()]
        context['rules_checkin'] = [rule for rule in Rule.objects.filter(rule_type='checkin')]
        context['rules_checkout'] = [rule for rule in Rule.objects.filter(rule_type='checkout')]
        context['rules_refund'] = [rule for rule in Rule.objects.filter(rule_type='refund')]
        context['rules_secure'] = [rule for rule in Rule.objects.filter(rule_type='secure')]
        return context

    def post(self, request, *args, **kwargs):
        try:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                info = get_bnb_info(request)
                category = Category.objects.filter(name=info['bnb_category']).first()
                location = Location(
                    name=info['bnb_location']['name'],
                    lat=info['bnb_location']['lat'],
                    lon=info['bnb_location']['lon'],
                )
                service = [Service.objects.filter(id=service).first() for service in info['list_service_id']]
                rules = [Rule.objects.filter(id=rule_id) for rule_id in info['rules']]

                new_bnb = BnbInformation(
                    name=info['bnb_name'],
                    description=info['bnb_description'],
                    price=float(info['bnb_price']),
                    capacity=int(info['bnb_capacity']),
                    category=category,
                    location=location,
                    services=service,
                    rules = rules,
                )

                new_bnb.save()
                for img in info['images']:
                    image = Image(
                        url=img,
                        product=new_bnb
                    )
                    image.sa

                return JsonResponse({'result': True}, status=200)
            else:
                return JsonResponse({'result': False}, status=400)
        except (ValueError, KeyError) as e:
            return JsonResponse({'result': False}, status=400)


def get_bnb_info(request):
    # additional_info = {}
    # for key, value in request.POST.items():
    #     if key.startswith('additionalInfo['):
    #         keys = key.replace('additionalInfo[', '').replace(']', '').split('[')
    #         ref = additional_info
    #         for k in keys[:-1]:
    #             ref = ref.setdefault(k, {})
    #         ref[keys[-1]] = value

    return {
        'bnb_name': request.POST.get('name'),
        'bnb_description': request.POST.get('description'),
        'bnb_location': request.POST.get('location'),
        'bnb_category': request.POST.get('categoryId'),
        'list_service_id': request.POST.get('listBnbService'),
        'rules': request.POST.getList('rules'),
        'owner_id': request.POST.get('ownerId'),
        'images': upload_image_using_cloudinary(request.FILES.getlist('images'), request.POST.get('name')),
    }


def upload_image_using_cloudinary(images, bnb_name):
    list_url = []
    for index, image in enumerate(images):
        public_id = f'bnb_images/{bnb_name.replace(" ", "_")}-image-{index + 1}'
        result = upload(image, public_id=public_id, overwrite=True)  # overwrite=True để ghi đè nếu trùng
        list_url.append(result['secure_url'])
    return list_url
