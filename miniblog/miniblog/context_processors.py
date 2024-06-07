from django.core.cache import cache

from product.models import Product, Category

def all_names_product(request):
    products = cache.get('products')
    if products in None:
        products = Product.objects.all().values_list('name')
        cache.set('products', products, 36000)
    return dict(
        names=products
    )

def all_names_category(request):
    categories = Category.objects.all()
    names = [category.name for category in categories]
    return dict(
        names_category=names
    )
