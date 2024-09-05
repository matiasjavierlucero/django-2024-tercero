from rest_framework.viewsets import ModelViewSet

from api_v1.serializers.product_serializer import ProductSerializer
from product.models import Product

class ProducViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer