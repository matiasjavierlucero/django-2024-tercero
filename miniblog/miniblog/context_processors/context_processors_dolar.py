import requests
from django.core.cache import cache

from product.models import Product

def dolar_exchange_rates(request):
    # BUSCO EN CACHE
    exchange_rates = cache.get('exchange_rates')
    # SI NO ENCUENTRO
    if exchange_rates is None:
        # LLAMO A LA API Y LE ASIGNO A LA VARIABLE EL JSON
        exchange_rates = requests.get("https://dolarapi.com/v1/dolares").json()
        #ALMACENO LA DATA EN CACHE
        cache.set('exchange_rates', exchange_rates, 600)
    return dict(
        valores_dolar=exchange_rates
    )
