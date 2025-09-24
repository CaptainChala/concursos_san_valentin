from rest_framework import serializers
from .models import Participante


class ParticipanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participante
        fields = [
            "id",
            "nombre_completo",
            "email",
            "telefono",
            "verificado",
            "creado_en",
        ]
        read_only_fields = ["id", "verificado", "creado_en"]
