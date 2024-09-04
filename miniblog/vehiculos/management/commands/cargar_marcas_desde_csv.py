import csv

from django.core.management.base import BaseCommand, CommandParser

from vehiculos.models import Marca


class Command(BaseCommand):
    help = "Es un comando encargado de cargar el modelo Marca a partir de un csv"
    

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            'archivo_csv',
            type=str,
            help="Archivo csv desde donde se va a cargar el modelo Marcas"
        )

    def handle(self, *args, **kwargs) -> str | None:
        self.stdout.write(self.style.WARNING('Iniciando Carga de Marcas'))
        csv_file = kwargs['archivo_csv']
        
        with open(csv_file, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                nombre_marca = row['Marca']
                marca = Marca.objects.get_or_create(nombre=nombre_marca)
                self.stdout.write(self.style.SUCCESS(f'Se cargo la marca {marca}'))

        self.stdout.write(self.style.WARNING('Finalizada Carga de Marcas'))
