from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.templatetags.i18n import language
from django.views.generic import TemplateView
from config.project_config import PROJECT_ENVIRONMENT
import json, time, requests

# Create your views here.
class SimpleView(TemplateView):
    template_name = "base.html"

    # Mỗi khi load home thì sẽ gọi function này ra để kiểm tra
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # if context_data['weather_data']: return context_data
        # cache_data = {}
        # if request.method == 'GET' and (
        #         cache_data.upload_time == False or time.time() - cache_data.upload_time <= 3600):
        #     location = request.content_params['location']
        #     lang = request.content_params['lang']
        # location = kwargs.get('location')
        # language = kwargs.get('language')

        location = "Ho Chi Minh"
        lang = "vi"

        # PROJECT_ENVIRONMENT là 1 file python (dùng tạm)
        result = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={PROJECT_ENVIRONMENT["open_weather"]}&lang={lang}&units=metric')
        cache_data = json.dumps(result.json())
        # cache_data.upload_time = time.time()
        context_data['weather_data'] = cache_data
        return context_data


    # Store a cache into a json


class SimpleComplexView(TemplateView):
    template_name = "sample_page.html"

