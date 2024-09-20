import factory
from factory.django import DjangoModelFactory

from product.models import Category, Product


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category
    name = factory.Sequence(lambda n: 'Category_%d' %n)

class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Sequence(lambda n: 'Product_%d' %n)
    price = factory.Faker('pyfloat', left_digits=2, right_digits=2, positive=True)
    category = factory.SubFactory(CategoryFactory)
