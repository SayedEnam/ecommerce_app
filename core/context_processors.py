from core.models import Product, Category, Brand, CartOrder, CartOrderItems, ProductImages, ProductReview, wishlist, Address

def default(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()

    return {
        'categories':categories,
        'brands':brands,
    }