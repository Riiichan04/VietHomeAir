from django.views.generic import TemplateView
import json
from django.shortcuts import render

class InfoOwnerBnBView(TemplateView):
    template_name = "application/templates/info-owner-bnb.html"

def onwer_review(request):
    # Đọc dữ liệu từ tệp JSON
    with open('application/static/data/BnbOwner.json', 'r', encoding='utf-8') as f:
        owners = json.load(f)

    # Trả lại template và truyền dữ liệu onwer
    return render(request, 'info-owner-bnb.html', {'owners': owners})