import os
import django

def create_superuser():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.base')
    django.setup()

    from django.contrib.auth import get_user_model
    from django.db import IntegrityError

    User = get_user_model()

    username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
    email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
    password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

    if not username or not email or not password:
        print("Erro: Variáveis de ambiente DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL e DJANGO_SUPERUSER_PASSWORD devem estar definidas.")
        return

    try:
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            print(f"Superusuário '{username}' criado com sucesso.")
        else:
            print(f"Superusuário '{username}' já existe.")
            return  
    except IntegrityError:
        print(f"Erro: Superusuário '{username}' já existe.")
        return 

if __name__ == "__main__":
    create_superuser()