from django.db.models import fields
from rest_framework import serializers
from rest_framework.generics import RetrieveAPIView

from .models import Animales


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animales
        fields = (
            'id',
            'nombre',
            'tipo',
            'raza',
            'sexo',
            'castrado',
            'color',
            'fecha_nacimiento',
            'observaciones'
        )


class AnimalnRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animales
        fields = (
            '__all__'
        )


class AnimalCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animales
        fields = (
            '__all__'
        )
