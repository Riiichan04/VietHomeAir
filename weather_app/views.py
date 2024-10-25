from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class SimpleView(TemplateView):
    template_name = "base.html"

class SimpleComplexView(TemplateView):
    template_name = "sample_page.html"

# Store a cache into a json
# import json, time
# x = {}
#
# def fetch_openweather_data_view(request):
#     if request.method == 'GET' and (x.upload_time == False or time.time() - x.upload_time <= 3600 ):
#         location = request.content_params['location']
#         lang = request.content_params['lang']
#         upload_date = time.time()
