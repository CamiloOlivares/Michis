from applications.animales.models import Animales
from django.shortcuts import render

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

from .serializers import AnimalCreateSerializer, AnimalSerializer, AnimalnRetrieveSerializer
# Create your views here.


class AnimalListApiView(ListAPIView):

    serializer_class = AnimalSerializer

    def get_queryset(self):
        return Animales.objects.all()


class AnimalRetrieveAPIView(RetrieveAPIView):
    serializer_class = AnimalnRetrieveSerializer
    queryset = Animales.objects.filter()


class AnimalCreateAPIView(CreateAPIView):
    serializer_class = AnimalCreateSerializer
