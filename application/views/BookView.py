import json
from django.views.generic import TemplateView
from django.shortcuts import render
class BookView(TemplateView):
    template_name = 'application/templates/Book.html'

def booking_view(request):
    # Đọc dữ liệu từ tệp JSON
    with open('application/models/HomeDataInVN.json', 'r', encoding='utf-8') as f:
        products = json.load(f)

    # Trả lại template và truyền dữ liệu sản phẩm
    return render(request, 'Book.html', {'products': products})
