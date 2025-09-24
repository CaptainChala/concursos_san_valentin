from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
import random
from django.shortcuts import get_object_or_404
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Participante, User
from .serializers import ParticipanteSerializer
from .tasks import enviar_correo_verificacion, enviar_correo_ganador
from django.contrib.auth import authenticate


class SetPasswordView(APIView):
    def post(self, request):
        import jwt
        from django.conf import settings

        token = request.data.get("token")
        password = request.data.get("password")
        if not token or not password:
            return Response({"error": "Token y contraseña son requeridos."}, status=400)
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            participante = get_object_or_404(
                Participante, id=payload["user_id"], email=payload["email"]
            )
            if not participante.verificado:
                return Response({"error": "Usuario no verificado."}, status=400)

            # Guardar contraseña en Participante
            participante.password = make_password(password)
            participante.verificado = True
            participante.save()

            return Response(
                {
                    "message": "Contraseña creada y cuenta activada. Usted ya se encuentra participando."
                }
            )
        except jwt.InvalidTokenError:
            return Response({"error": "Token inválido."}, status=400)


class RegistroParticipanteView(generics.CreateAPIView):
    serializer_class = ParticipanteSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"detail": "Registro exitoso. Revisa tu correo para verificar."},
            status=status.HTTP_201_CREATED,
            headers=headers,
        )

    def perform_create(self, serializer):
        participante = serializer.save()
        enviar_correo_verificacion.delay(participante.id)


class VerificarCorreoView(APIView):
    def get(self, request):
        import jwt
        from django.conf import settings

        token = request.query_params.get("token")
        if not token:
            return Response({"error": "Token no proporcionado."}, status=400)
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            participante = get_object_or_404(
                Participante,
                id=payload["user_id"],
                email=payload["email"],
                verificacion_token=token,
            )
            participante.verificado = True
            participante.verificacion_token = None
            participante.save()
            return Response(
                {"message": "Correo verificado. Ahora puedes crear tu contraseña."}
            )
        except jwt.ExpiredSignatureError:
            return Response({"error": "El token ha expirado."}, status=400)
        except jwt.InvalidTokenError:
            return Response({"error": "Token inválido."}, status=400)


class ListaParticipantesAdminView(generics.ListAPIView):
    queryset = Participante.objects.all()
    serializer_class = ParticipanteSerializer


# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from participantes.models import Participante
from django.core.mail import send_mail
import random

class SorteoGanadorView(APIView):
    # authentication_classes = [TokenAuthentication]  # opcional
    # permission_classes = [IsAdminUser]  # opcional

    def post(self, request):
        participantes = Participante.objects.filter(verificado=True)
        if not participantes.exists():
            return Response({"error": "No hay participantes verificados"}, status=400)

        ganador = random.choice(participantes)
        
        # Enviar correo
        send_mail(
            subject="¡Felicidades! Ganaste el sorteo",
            message=f"Hola {ganador.nombre_completo},\n¡Has ganado el sorteo!",
            from_email="no-reply@sorteo.com",
            recipient_list=[ganador.email],
            fail_silently=True,
        )

        return Response({
            "nombre": ganador.nombre_completo,
            "email": ganador.email
        })



class AdminLoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"error": "Username y contraseña son requeridos"}, status=400
            )

        # Autenticación usando username
        user = authenticate(request, username=username, password=password)

        if user and user.is_staff:
            return Response({"message": "Login exitoso"})
        return Response({"error": "Credenciales inválidas"}, status=400)
