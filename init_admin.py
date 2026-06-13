import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.contrib.auth import get_user_model

def create_admin():
    User = get_user_model()
    
    username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin')
    password = os.getenv('DJANGO_SUPERUSER_PASSWORD')
    # email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
    
    if not password:
        print("Пропуск: DJANGO_SUPERUSER_PASSWORD не задан в переменных окружения.")
        return

    if not User.objects.filter(username=username).exists():
        print(f"Создание суперпользователя '{username}'...")
        User.objects.create_superuser(username=username, email=email, password=password)
        print("Суперпользователь успешно создан.")
    else:
        print(f"Суперпользователь '{username}' уже существует в базе данных.")

if __name__ == '__main__':
    create_admin()
