from typing import List, Optional, NoReturn

from product.models import Category

class CategoryRepository:

    def get_all(self) -> List[Category]:
        return Category.objects.all()

    def get_by_id(self, id: int) -> Optional[Category]:
        return Category.objects.get(pk=id)

    def delete(self, category: Category):
        category.delete()

    def update(
        self,
        category: Category,
        nombre: str,
    ):
        category.name = nombre
        category.save()

    def create(
        self,
        nombre: str
    ) -> Category:
        category = Category.objects.filter(name=nombre)
        if category:
            return "CHE EL NOMBRE ESTA OCUPADO"
        return Category.objects.create(
            name=nombre,
        )

