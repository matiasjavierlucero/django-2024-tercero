from django.contrib import admin

from vehiculos.models import Marca, Vehiculo

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)


@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('marca','modelo','cilindrada')
