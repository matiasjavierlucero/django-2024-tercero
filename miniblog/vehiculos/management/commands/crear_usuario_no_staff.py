from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Es un comando encargado de crear un usuario no staff"
    

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            'username',
            type=str,
            help="Nombre de Usuario"
        )
        parser.add_argument(
            'password',
            type=str,
            help="Password"
        )

    def handle(self, *args, **kwargs) -> str | None:
        self.stdout.write(self.style.WARNING('Creando usuario'))
        nombre = kwargs['username']
        password = kwargs['password']
        
        usuario = User.objects.create(
            username=nombre,
            is_staff=False,
        )
        usuario.set_password(password)
        

        self.stdout.write(self.style.WARNING(f'Usuario {usuario.username} Creado '))
