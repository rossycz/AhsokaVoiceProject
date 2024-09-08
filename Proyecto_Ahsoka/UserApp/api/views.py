from rest_framework import viewsets
from UserApp.models import user
from UserApp.api.serializer import UserSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = UserSerializer