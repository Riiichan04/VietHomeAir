from django.views.generic import TemplateView
from application.models import BnbInformation
class BnbInfoView(TemplateView):
    template_name = "application/templates/bnb-information.html"

    def get_bnb_name(self, bnb_id):
        bnb = BnbInformation.objects.get(id=bnb_id)
        return bnb if bnb is not None else None
