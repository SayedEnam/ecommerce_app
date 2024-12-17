from django.urls import path
from core.views import index, category_list_view, product_list_view, category_product_list_view, brand_list_view
from . import views


app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('products/', product_list_view, name='product-list'),
    path('categories/', category_list_view, name='categories-list'),
    path('categories/<cid>/', category_product_list_view, name='category-product-list-view'),
    path('brands/', brand_list_view, name='brand-list-view'),
]