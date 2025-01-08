from django.http import Http404, JsonResponse
from django.views.generic import TemplateView

from application.services.category_service import get_category, get_bnb_by_category, get_category_original_name


class CategoryView(TemplateView):
    template_name = "application/templates/category.html"

    def get_context_data(self, **kwargs):
        category_name = self.kwargs['category_name']
        category = get_category(category_name)
        if category is None: raise Http404("Tìm cái j thế?")
        list_bnb_data = get_bnb_by_category(category_name)
        context = super().get_context_data(**kwargs)
        context['category_name'] = get_category_original_name(category)
        context['list_bnb_data'] = list_bnb_data
        return context

    def get(self, request, *args, **kwargs):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            category_name = self.kwargs['category_name']
            if get_category(category_name) is None: raise Http404("Tìm cái j thế?")
            current_offset = request.GET.get('currentOffset')
            listBnbData = get_bnb_by_category(category_name, offset=int(current_offset))
            if listBnbData is None:
                return JsonResponse({'result': False, 'otherBnb': []})
            else:
                list_bnb_info = []
                for bnb in listBnbData:
                    bnb_info_converted = {
                        'id': bnb.id,
                        'price': bnb.price + ' VNĐ',
                        'lat': f'{bnb.location.lat}'.replace(',', '.'),
                        'lon': f'{bnb.location.lon}'.replace(',', '.'),
                        'name': bnb.name,
                        'thumbnail': bnb.thumbnail,
                        'listImage': [image for image in bnb.list_image],
                        'owner': bnb.owner,
                        'avgRating': bnb.avg_rating + '/5'
                    }
                    list_bnb_info.append(bnb_info_converted)
                return JsonResponse({'result': True, 'otherBnb': list_bnb_info})

        # Không phải ajax thì trả về trang bình thường
        else:
            return super().get(request, *args, **kwargs)
