from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from Catalog.models import Product


class ProductListView(ListView):
    paginate_by = 20
    model = Product
    template_name = 'Front/catalog.html'
    context_object_name = 'products'
    ordering = ['created_at']

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        result = super().get(request, *args, **kwargs)
        return result


class ProductDetailView(DetailView):
    model = Product
    template_name = 'Front/product.html'
    context_object_name = 'product'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().get(request, *args, **kwargs)


# Create your views here.
def index(request):
    return render(request, 'Front/index.html')
