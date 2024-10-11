import csv

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend

from api_v1.filters import ProductFilter
from api_v1.serializers.product_serializer import ProductSerializer
from product.models import Category ,Product


class ProductModelViewSet(ModelViewSet):
    # GET(LIST); POST(CREATE); PUT(UPDATE); PATCH(PARTIAL UPDATE); DELETE(DESTROY) Y UN DETAIL(RETRIEVE)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'stock', 'category__name']
    filterset_class = ProductFilter
    
    def create(self, request, *args, **kwargs):
        # Extraemos los datos de la peticion
        data = request.data

        # Extraemos o creamos la categoria
        category_data = data.get('category')

        if len(category_data) > 0:
            category_name = category_data.get('name')
            category, created = Category.objects.get_or_create(
                name=category_name
                )
        category = None
        # Creamos el producto
        product = Product.objects.create(
            name=data.get('name'),
            description=data.get('description', None),
            price=data.get('price'),
            stock=data.get('stock'),
            active=data.get('active', True),
            category=category or None
        )

        serializer = self.serializer_class(product)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['get'], detail=False, url_path='download-csv')
    def download_csv(self, request):
        # Defino que voy a retornar y bajo que nombre
        categoria = request.query_params.get('category', None)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="product.csv"'

        writer = csv.writer(response)
        writer.writerow(
            [
                "Nombre", "Descripcion", "Precio", "Categoria", "Stock"
            ]
        )
        products = self.get_queryset()
        if categoria:
            products = self.get_queryset().filter(category__name=categoria)

        for product in products:
            writer.writerow(
            [
                product.name,
                product.description, 
                product.price, 
                product.category.name if product.category else 'No posee', 
                product.stock,
            ]
        )
        return response
    
    @action(detail=False, methods=['get'], url_path='download-price-stock-csv')
    def download_price_stock(self, request):

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="total_price_stock.csv"'

        file = csv.writer(response)
        file.writerow(
            [
                "Nombre",
                "Precio",
                "Cantidad",
                "Valor Total"
            ]
        )
        for product in self.get_queryset():
            file.writerow(
                [
                    product.name,
                    product.price,
                    product.stock,
                    product.price * product.stock
                ]
            )
        return response
    
    @action(methods=['get'], detail=False, url_path='latest')
    def last_product(self, request):
        last_product = self.get_queryset().last()
        serializer = self.serializer_class(last_product)
        return Response(serializer.data)
    

## VISTA UTILIZANDO APIView
from rest_framework.views import APIView
    
class ProductApiView(APIView):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        product_id = self.kwargs.get('pk', None)
        if product_id:
            products = products.get(id=product_id)
            serializer = ProductSerializer(products)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data

        # Extraemos o creamos la categoria
        category_data = data.get('category')

        if len(category_data) > 0:
            category_name = category_data.get('name')
            category, created = Category.objects.get_or_create(
                name=category_name
                )
        category = None
        # Creamos el producto
        product = Product.objects.create(
            name=data.get('name'),
            description=data.get('description', None),
            price=data.get('price'),
            stock=data.get('stock'),
            active=data.get('active', True),
            category=category or None
        )

        serializer = ProductSerializer(product)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )
    
## UTILIZANDO GENERIC API VIEWS
from rest_framework import generics
from rest_framework import mixins

class ProductListCreateGenericAPIView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        product_id = self.kwargs.get('pk', None)
        if product_id:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


## READ ONLY MODEL VIEW SET
class ProductReadOnly(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
