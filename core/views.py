from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count

from core.models import Product, Category, Brand, CartOrder, CartOrderItems, ProductImages, ProductReview, wishlist, Address


def index(request):
    #products = Product.objects.all().order_by("-id")
    products = Product.objects.filter(product_status="published", featured=True).order_by("-id")

    context = {
        'products':products
    }
    return render(request, 'core/index.html', context)

def product_list_view(request):
    products = Product.objects.filter(product_status="published")

    context = {
        'products': products
    }

    return render(request, 'core/product-list.html', context)

def category_list_view(request):
    categories = Category.objects.all().annotate(product_count=Count("category"))

    context = {
        'categories': categories
    }
    return render(request, 'core/categories-list.html', context)


def category_product_list_view(request, cid):
    category = Category.objects.get(cid=cid)
    products = Product.objects.filter(product_status="published", category=category)

    context = {
        'category':category,
        'products':products,
    }

    return render(request, "core/category-product-list-view.html", context)


def brand_list_view(request):
    brands = Brand.objects.all()

    context = {
        'brands': brands,
    }
    return render(request, 'core/brand-list-view.html', context)
