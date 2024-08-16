from rest_framework import viewsets
from UsuarioApp.models import usuario
from UsuarioApp.api.serializer import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = UsuarioSerializer