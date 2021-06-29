from rest_framework import serializers

from .models import Cliente


class ClienteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nome', 'id', 'idade', 'cidade']
        read_only_fields = fields


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nome', 'idade', 'cidade']
