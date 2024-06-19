from product.models import Product

def all_products_names(request):
    return dict(
        nombres_productos = Product.objects.all().values_list("name")
    )
