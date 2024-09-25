from decimal import Decimal
import pytest

from django.urls import reverse
from rest_framework import status 
from rest_framework.test import APIClient

from api_v1.tests.factories import ProductFactory, CategoryFactory
from product.models import Product


def test_first_test():
    assert 3 == 3


#ARRANGE, ACT, ASSERT
@pytest.mark.django_db
def test_list_products(client: APIClient):
    # Arrange
    product_1 = ProductFactory()
    product_2 = ProductFactory()
    # Act
    url = reverse('products-list')
    response = client.get(path=url)
    # Assert
    expected_result = {
        'count':2,
        'next': None,
        'previous': None,
        'results':[
            {
                "id": product_1.id,
                "category": {
                    "name":product_1.category.name,
                    "pk": product_1.category.pk
                },
                "description": "No posee descripción",
                "name": product_1.name,
                "price": f"{product_1.price}",
                "stock": 0,
                "active": True
            },
            {
                "id": product_2.id,
                "category": {
                    "name":product_2.category.name,
                    "pk": product_2.category.pk
                },
                "description": "No posee descripción",
                "name": product_2.name,
                "price":f"{product_2.price}",
                "stock": 0,
                "active": True
            }
        ]
    }
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_result

@pytest.mark.django_db
def test_detail_products(client: APIClient):
    # Arrange
    product_1 = ProductFactory()
    product_2 = ProductFactory()
    product_3 = ProductFactory()
    product_4 = ProductFactory()
    # Act
    url = reverse('products-detail', args=(product_2.pk,))
    response = client.get(path=url)
    # Assert
    expected_result = dict(
        name=product_2.name,
        description="No posee descripción",
        active=True,
        stock=0,
        price=f'{product_2.price}',
        category=dict(
            name=product_2.category.name,
            pk=product_2.category.id
        ),
        id=product_2.id
    )
    
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_result

@pytest.mark.django_db
def test_delete_products(client: APIClient):
    # Arrange
    product_1 = ProductFactory()
    product_2 = ProductFactory()
    product_3 = ProductFactory()
    product_4 = ProductFactory()
    # Act
    url = reverse('products-detail', args=(product_2.pk,))
    response = client.delete(path=url)

    products = Product.objects.all()
    assert products.count() == 3
    assert product_2 not in products

@pytest.mark.django_db
def test_create_products(client: APIClient):
    for x in range(10):
        ProductFactory()

    data = {
        "category":{},
        "name":"product test name",
        "price": 1234,
        "stock": 1234,
    }
    url = reverse('products-list')
    response = client.post(
        path=url,
        data=data,
        content_type='application/json'
    )

    assert response.status_code == status.HTTP_201_CREATED

    assert Product.objects.count() == 11