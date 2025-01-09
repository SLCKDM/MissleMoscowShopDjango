from django.urls import path, include

from . import views

app_name = 'Front'
urlpatterns = [
    path('', views.index, name='index'),
    path('faq', views.index, name='faq'),
    path('catalog', views.ProductListView.as_view(), name='catalog'),
    path('catalog/<str:pk>', views.ProductDetailView.as_view(), name='product'),
]
