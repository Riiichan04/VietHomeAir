from django.views.generic import  TemplateView
from django.shortcuts import render

class OwnerRegisterView(TemplateView):
    template_name = 'application/templates/OwnerRegister.html'

    def get_bnb_display_element(bnb_id):
        try:
            bnb = BnbInformation.objects.get(id=bnb_id)
            return {
                'id': bnb.id,
                'name': bnb.name,
                'description': bnb.description,
                'price': bnb.price,
                'location': bnb.location.name,
                'views': bnb.count_viewed,
                'rating': getattr(bnb, 'rating', 0)  # Nếu có trường rating
            }
        except BnbInformation.DoesNotExist:
            return None


