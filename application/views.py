from django.views.generic import TemplateView
from dotenv import load_dotenv, find_dotenv
import os, json, time, requests
from application.module.cache_operator import is_need_renew_weather_cache_data, find_cache_data

load_dotenv(find_dotenv())
# Create your views here.
class SimpleView(TemplateView):
    template_name = "application/templates/base.html"

    # Mỗi khi load home thì sẽ gọi function này ra để kiểm tra
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        cache_data = find_cache_data(os.getcwd() + '/application/data')
        if is_need_renew_weather_cache_data(cache_data):
            location = "Ho Chi Minh"
            lang = "vi"
            OPENWEATHER_KEY = os.getenv("OPEN_WEATHER")

            result = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={OPENWEATHER_KEY}&lang={lang}&units=metric')
            result_data = result.json()
            result_data.update({"upload_time": int(time.time())})

            cache_data = {'weather_data': result_data}

            with open(os.getcwd() + '/application/data/cache_data.json', 'w', encoding='utf-8') as f:
                json.dump(cache_data, f, ensure_ascii=False, indent=4)

        context_data['weather_data'] = cache_data
        return context_data


class SimpleComplexView(TemplateView):
    template_name = "application/templates/frontend_test.html"

