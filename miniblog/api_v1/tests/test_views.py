from decimal import Decimal
import pytest

from django.urls import reverse
from rest_framework import status 
from rest_framework.test import APIClient

from api_v1.tests.factories import ProductFactory
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
def test_create_product(client: APIClient):
    # Arrange
    data_1 = {
        "category": {},
        "name": "Test Product",
        "price": 1234,
        "stock": 555,
        "description": "test_description"
    }
    data_2 = {
        "category": {},
        "name": "Test Product 2",
        "price": 1234,
        "stock": 555,
        "description": "test_description"
    }

    # Act
    url = reverse('products-list')
    client.post(
        path=url,
        data=data_1,
        content_type="application/json"
    )
    response = client.post(
        path=url,
        data=data_2,
        content_type="application/json"
    )
    #Assert
    assert response.status_code is status.HTTP_201_CREATED
    products = Product.objects.all()
    assert products.count() == 2
    assert products.first().name == 'Test Product'
    assert products.last().name == 'Test Product 2'

@pytest.mark.django_db
def test_detail_product_without_category(client: APIClient):
    product_1 = ProductFactory(category=None)
    product_2 = ProductFactory(category=None)
    product_3 = ProductFactory(category=None)

    url = reverse('products-detail', args=(product_1.pk,))
    response = client.get(url)

    expected_result = dict(
        id=product_1.id,
        name=product_1.name,
        price=f'{product_1.price}',
        description="No posee descripción",
        stock=product_1.stock,
        active=True,
        category=None
    )

    assert response.json() == expected_result

@pytest.mark.django_db
def test_detail_product_with_category(client: APIClient):
    product_1 = ProductFactory(name="Nombre forzado", category=None)
    product_2 = ProductFactory()
    product_3 = ProductFactory()

    url = reverse('products-detail', args=(product_1.pk,))
    response = client.get(url)

    expected_result = dict(
        id=product_1.id,
        name="Nombre forzado",
        price=f'{product_1.price}',
        description="No posee descripción",
        stock=product_1.stock,
        active=True,
        category=None
    )

    assert response.json() == expected_result

    url = reverse('products-detail', args=(product_2.pk,))
    response = client.get(url)

    expected_result = dict(
        id=product_2.id,
        name=product_2.name,
        price=f'{product_2.price}',
        description="No posee descripción",
        stock=product_2.stock,
        active=True,
        category=dict(
            name=product_2.category.name,
            pk=product_2.category.pk
        )
    )

    assert response.json() == expected_result

@pytest.mark.django_db
def test_delete_product(client: APIClient):
    product_1 = ProductFactory()
    product_2 = ProductFactory()
    product_3 = ProductFactory()

    url = reverse('products-detail', args=(product_1.pk,))
    response = client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    products = Product.objects.all()
    assert products.count() == 2
    product = Product.objects.filter(id=product_1.id)
    assert product.count() == 0
    assert product_2 in products
    assert product_3 in products
    assert product_1 not in products
