from django.db import models


class ProductQuerySet(models.QuerySet):

    def actives(self):
        return self.filter(active=True)
    
    def inactive(self):
        return self.filter(active=False)

    def price_total(self):
        total = 0
        for producto in self:
            total += producto.price
        return total
