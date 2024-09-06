from rest_framework import serializers

from product.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_description(self, value):
        if value.description is None:
            return "No posee descripción"
        return value.description

    def update(self, instance, validated_data):
        category_data = validated_data.pop(
            'category', None
        )
        category, _= Category.objects.get_or_create(
          **category_data
        )

        instance.category = category

        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.active = validated_data.get('active', instance.active)
        instance.stock = validated_data.get('stock', instance.stock)

        instance.save()
        return instance
