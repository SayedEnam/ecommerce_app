from django.shortcuts import render, get_object_or_404
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


def brand_product_list_view(request, bid):
    brand = Brand.objects.get(bid=bid)
    products = Product.objects.filter(product_status="published", brand=brand)

    context = {
        'brand':brand,
        'products':products,
    }

    return render(request, "core/brand-product-list-view.html", context)


def product_detail_view(request, pid):
    product = Product.objects.get(pid=pid)
    # product = get_object_or_404(product, pid=pid)

    p_image = product.p_image.all()

    context = {
        'p': product,
        'p_image': p_image,
    }


    return render(request, 'core/product-detail.html', context)