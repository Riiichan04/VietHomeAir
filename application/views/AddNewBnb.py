from cloudinary.uploader import upload
from django.http import JsonResponse
from django.views.generic import TemplateView

from application.models import BnbInformation, Owner, Account
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
        # try:
        #     if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                info = get_bnb_info(request)
                print(info)
                location = Location(
                    name=info['bnb_location']['name'],
                    lat=info['bnb_location']['lat'],
                    lon=info['bnb_location']['lon'],
                )
                location.save()
                category = [Category.objects.filter(id=int(category)).get() for category in info['bnb_categories']]
                service = [Service.objects.filter(id=int(service)).get() for service in info['list_service_id']]
                rules = [Rule.objects.filter(id=int(rule_id)).get() for rule_id in info['rules']]

                owner_account = Account.objects.filter(id=info['owner_id']).first()
                owner = Owner.objects.filter(account=owner_account).first()


                if owner is None:
                    new_owner = Owner(account=owner_account)
                    owner = new_owner
                    new_owner.save()

                new_bnb = BnbInformation.objects.create(
                    name=info['bnb_name'],
                    description=info['bnb_description'],
                    price=float(info['price']),
                    capacity=info['bnb_capacity'],
                    location=location,
                    owner=owner,
                )
                new_bnb.category.add(*category)
                new_bnb.service.add(*service)
                new_bnb.rule.add(*rules)
                for img in info['images']:
                    image = Image(
                        url=img,
                        product=new_bnb
                    )
                    image.save()
                location.save()
                new_bnb.save()
                return JsonResponse({'result': True}, status=200)
            # else:
            #     return JsonResponse({'result': False}, status=400)
        # except (ValueError, KeyError) as e:
        #     return JsonResponse({'result': False}, status=400)


def get_bnb_info(request):
    return {
        'bnb_name': request.POST.get('name'),
        'bnb_description': request.POST.get('description'),
        'bnb_location': {
            'name': request.POST.get('location_name'),
            'lat': float(request.POST.get('location_lat')),
            'lon': float(request.POST.get('location_lon')),
        },
        'bnb_capacity': int(request.POST.get('capacity')),
        'bnb_categories': request.POST.getlist('categories'),
        'list_service_id': request.POST.getlist('services'),
        'rules': request.POST.getlist('rules'),
        'owner_id': int(request.POST.get('ownerId')),
        'images': upload_image_using_cloudinary(request.FILES.getlist('images'), str(BnbInformation.objects.count())),
        'price': float(request.POST.get('price')),
    }


def upload_image_using_cloudinary(images, bnb_name):
    list_url = []
    folder_name = 'python-web-images/bnb-images/'
    for index, image in enumerate(images):
        public_id = f'bnb_images/{bnb_name.replace(" ", "_")}-image-{index + 1}'
        result = upload(image, folder=folder_name, public_id=public_id, overwrite=True)  # overwrite=True để ghi đè nếu trùng
        list_url.append(result['secure_url'])
    return list_url
