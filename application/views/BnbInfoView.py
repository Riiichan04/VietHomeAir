import os
import threading

from django import template

from django.http import Http404, JsonResponse
from django.views.generic import TemplateView
from application.models import BnbInformation
import application.services.bnb_info_service as bnb_service
from application.templatetags.bnb_info_filter import user_review_status


class BnbInfoView(TemplateView):
    template_name = "application/templates/bnb-information.html"

    def get_context_data(self, **kwargs):
        bnb = bnb_service.get_bnb_info(self.kwargs['bnbid'])
        if bnb is None: raise Http404("Eooooo, tìm nhầm chỗ rồi")
        context = super().get_context_data(**kwargs)
        context['bnb'] = bnb
        context['google_map_key'] = os.getenv('GOOGLE_MAP_API_KEY')
        context['other_bnb'] = bnb_service.get_similar_bnb(bnb['id'])
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
        else:
            return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            if (request.headers.get('X-Requested-With') == 'XMLHttpRequest'
                    and user_review_status(request.session, int(self.kwargs['bnbid']))):
                threading.Thread(
                    target=bnb_service.validate_review,
                    args=({
                              'rating': request.POST.get('rating'),
                              'content': request.POST.get('content'),
                              'accountId': request.POST.get('accountId'),
                              'bnbId': request.POST.get('bnbId')
                          },)
                ).start()
                return JsonResponse({'result': True}, status=200)
            else:
                return JsonResponse({'result': False}, status=400)
        except (ValueError, KeyError) as e:
            return JsonResponse({'result': False}, status=400)
