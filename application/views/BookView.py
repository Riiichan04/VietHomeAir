import json
from django.views.generic import TemplateView
from django.shortcuts import render
class BookView(TemplateView):
    template_name = 'application/templates/booking.html'

def booking_view(request):
    # Đọc dữ liệu từ tệp JSON
    with open('application/static/data/data.json', 'r', encoding='utf-8') as f:
        products = json.load(f)

    # Trả lại template và truyền dữ liệu sản phẩm
    return render(request, 'booking.html', {'products': products})
