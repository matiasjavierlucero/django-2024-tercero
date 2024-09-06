from rest_framework.viewsets import ModelViewSet
from api_v1.paginations import MiPaginador

from api_v1.serializers.product_serializer import ProductSerializer
from product.models import Category ,Product

class ProducViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
