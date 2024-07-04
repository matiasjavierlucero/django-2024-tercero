import csv

from django.core.management.base import BaseCommand, CommandParser

from vehiculos.models import Marca, Vehiculo

class Command(BaseCommand):
    help = "Es un comando encargado de cargar Vehiculos a partir de un csv"
    

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            'archivo_csv',
            type=str,
            help="Archivo csv desde donde se va a cargar el modelo Vehiculos"
        )

    def handle(self, *args, **kwargs) -> str | None:
        self.stdout.write(self.style.WARNING('Iniciando Carga de Vehiculo'))
        csv_file = kwargs['archivo_csv']
        
        with open(csv_file, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                nombre_marca = row['Marca']
                marca = Marca.objects.get(nombre=nombre_marca)
                vehiculo = Vehiculo.objects.get_or_create(
                    marca=marca,
                    modelo=row['Modelo'],
                    fabricado_el=row['Año de Fabricacion'],
                    cantidad_puertas=row['Cantidad de Puertas'],
                    cilindrada=row['Cilindrada'],
                    tipo_combustible=row['Tipo de Combustible'],
                    pais_fabricacion=row['Pais de Fabricacion'],
                    precio_dolares=row['Precio en dolares'],
                )

                self.stdout.write(self.style.SUCCESS(f'Se cargo la el vehiculo {vehiculo}'))

        self.stdout.write(self.style.WARNING('Finalizada Carga de Vehiculos'))
