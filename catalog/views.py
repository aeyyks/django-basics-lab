from django.shortcuts import render
from django.views.generic import DetailView

from .models import Product


# Create your views here.
def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'  # укажите путь к вашему шаблону
    context_object_name = 'product'  # имя переменной в шаблоне (по умолчанию 'object')
