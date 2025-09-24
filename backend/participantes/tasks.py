from celery import shared_task
from django.core.mail import send_mail
from .models import Participante


@shared_task
def enviar_correo_verificacion(participante_id):
    import jwt
    from django.conf import settings

    participante = Participante.objects.get(id=participante_id)

    token = jwt.encode(
        {"user_id": participante.id, "email": participante.email},
        settings.SECRET_KEY,
        algorithm="HS256",
    )
    participante.verificacion_token = token
    participante.save()

    enlace = f"http://localhost:3000/verificar/?token={token}"
    send_mail(
        subject="Verifica tu correo",
        message=f"Hola {participante.nombre_completo}, verifica tu cuenta aquí: {enlace}",
        from_email="noreply@concurso.com",
        recipient_list=[participante.email],
    )


@shared_task
def enviar_correo_ganador(participante_id):
    participante = Participante.objects.get(id=participante_id)
    send_mail(
        subject="¡Felicidades! Ganaste el sorteo 🎉",
        message=f"Hola {participante.nombre_completo}, ganaste el concurso de San Valentín.",
        from_email="noreply@concurso.com",
        recipient_list=[participante.email],
    )
