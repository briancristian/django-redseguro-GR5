from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Gestiones
from .serializers import GestionesSerializer

class GestionViewSet(viewsets.ModelViewSet):
    queryset = Gestiones.objects.all()
    serializer_class = GestionesSerializer