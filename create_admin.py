import os
import django

# Define as configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

# Importa o seu modelo de usuário customizado
from apps.usuarios.models import Usuario 

def create_superuser():
    username = 'eduardo'
    email = 'eduardo@email.com'
    password = 'duda12345678' # Altere para a senha que desejar

    if not Usuario.objects.filter(username=username).exists():
        Usuario.objects.create_superuser(
            username=username, 
            email=email, 
            password=password
        )
        print(f"Superusuário '{username}' criado com sucesso!")
    else:
        print(f"Superusuário '{username}' já existe.")

if __name__ == '__main__':
    create_superuser()