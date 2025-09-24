from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Participante


class ParticipanteTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.participante_data = {
            "nombre_completo": "Juan Pérez",
            "email": "juan@example.com",
            "telefono": "123456789",
        }

    def test_crear_participante(self):
        """Debe crear un participante nuevo"""
        response = self.client.post(
            reverse("registro"), self.participante_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Participante.objects.count(), 1)

    def test_evitar_registro_duplicado(self):
        """Debe rechazar un email duplicado"""
        self.client.post(reverse("registro"), self.participante_data, format="json")
        response = self.client.post(
            reverse("registro"), self.participante_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
