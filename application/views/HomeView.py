from django.views.generic import TemplateView

from application.models import BnbInformation


class HomeView(TemplateView):
    template_name = "application/templates/home.html"

    def get_display_bnb(self, bnb_id):
        bnb = BnbInformation.objects.get(id=bnb_id)
        owner = bnb.owner
        return {
            'id': bnb_id,
            'thumbnail': bnb.image_set.first().url,
            'name': bnb.name,
            # 'description': bnb.description,
            'owner': owner.account.fullname,
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Code tạm để báo cáo
        context['hotbnb'] = [self.get_display_bnb(bnb_id) for bnb_id in range(1, 6)]
        context['high_rated_bnb'] = [self.get_display_bnb(bnb_id) for bnb_id in range(6, 11)]
        context['otherbnb'] = [self.get_display_bnb(bnb_id) for bnb_id in
                               range(1, len(BnbInformation.objects.all()) + 1)]
        return context
