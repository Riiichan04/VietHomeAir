from django import template

from django.http import Http404, JsonResponse
from django.views.generic import TemplateView
from application.models import BnbInformation
import application.services.bnb_info_service as bnb_service


class BnbInfoView(TemplateView):
    template_name = "application/templates/bnb-information.html"

    def get_context_data(self, **kwargs):
        bnb = bnb_service.get_bnb_info(self.kwargs['bnbid'])
        if bnb is None: raise Http404("Eooooo, tìm nhầm chỗ rồi")
        context = super().get_context_data(**kwargs)
        context['bnb'] = bnb
        return context

    def get(self, request, *args, **kwargs):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            sentiment_type = request.GET.get('sentiment_type', None)
            review_statistic = bnb_service.statistic_review_by_id(self.kwargs['bnbid'])
            filtered_reviews = {}

            if sentiment_type == 'positive':
                filtered_reviews = review_statistic['pos_reviews']
            if sentiment_type == 'negative':
                filtered_reviews = review_statistic['neg_reviews']
            if sentiment_type == 'all':
                filtered_reviews = review_statistic['all_reviews']

            json_result = [
                {
                    'avatar': review.account.avatar,
                    'fullname': review.account.fullname,
                    'rating_content': bnb_service.display_review(review),
                    'content': review.content

                }
                for review in filtered_reviews['reviews']
            ]
            return JsonResponse({'reviews': json_result})

        # Không phải ajax thì trả về trang bình thường
        else: return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Gọi model AI lên xử lý
        # Xử lý và trả về result
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            bnb_service.validate_review({'rating': request.POST.get('rating'), 'content' : request.POST.get('content'), 'accountId': request.POST.get('accountId'), 'bnbId': request.POST.get('bnbId')})
            return JsonResponse({'result': True}, status=200) #Đã fix
        return JsonResponse({'result': False}, status=400)
