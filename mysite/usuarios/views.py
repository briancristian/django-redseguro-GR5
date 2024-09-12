# usuarios/views.py
from rest_framework import viewsets
from .models import Usuario
from .serializers import UsuarioSerializer
from django.shortcuts import render

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    

def index (req):
    return render(req, "registro.html")