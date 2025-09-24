from django.contrib.auth import get_user_model

User = get_user_model()

def run():
    email = "admin@correo.com"
    username = "admin"  # obligatorio
    password = "123456"

    if not User.objects.filter(email=email).exists():
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
            is_admin=True,   # opcional según tu modelo
            is_staff=True,
            is_superuser=True
        )
        print(f"Admin creado: {email}")
    else:
        print(f"Admin ya existe: {email}")
