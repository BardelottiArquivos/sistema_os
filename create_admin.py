import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from apps.usuarios.models import Usuario

def create_superuser():
    username = 'admin_render'
    email = 'admin@exemplo.com'
    password = 'Render2026!'
    
    if not Usuario.objects.filter(username=username).exists():
        Usuario.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        print(f"✅ Superusuário '{username}' criado com sucesso!")
        print(f"🔑 Senha: {password}")
    else:
        print(f"⚠️ Usuário '{username}' já existe.")

if __name__ == '__main__':
    create_superuser()