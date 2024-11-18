from django.views.generic import TemplateView

class ProductView(TemplateView):
    template_name = "application/templates/product.html"