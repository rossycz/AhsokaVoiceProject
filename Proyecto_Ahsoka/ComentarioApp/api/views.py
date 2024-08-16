from rest_framework import viewsets
from ComentarioApp.models import comentario
from ComentarioApp.api.serializer import ComentarioSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = comentario.objects.all()
    serializer_class = ComentarioSerializer
    