import factory
from factory.django import DjangoModelFactory

from product.models import Product, Category


class CategoryFactory(DjangoModelFactory):

    class Meta:
        model = Category

class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Sequence(lambda n: 'Product_%d' %n)
    price = factory.Faker('pyfloat', left_digits=2, right_digits=2, positive=True)
    category = factory.SubFactory(CategoryFactory)
