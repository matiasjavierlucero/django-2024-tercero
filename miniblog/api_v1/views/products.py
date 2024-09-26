import csv

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend

from api_v1.filters import ProductFilter
from api_v1.serializers.product_serializer import ProductSerializer
from product.models import Category ,Product


class ProducViewSet(ModelViewSet):
    # GET(LIST); POST(CERATE); PUT(UPDATE); PATCH(PARTIAL UPDATE); DELETE(DESTROY) Y UN DETAIL(RETRIEVE)
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
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="product.csv"'

        writer = csv.writer(response)
        writer.writerow(
            [
                "Nombre", "Descripcion", "Precio", "Categoria", "Stock"
            ]
        )
        for product in self.get_queryset():
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