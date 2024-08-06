from rest_framework import viewsets
from LogroApp.models import logro
from LogroApp.api.serializer import LogroSerializer    

class LogroViewSet(viewsets.ModelViewSet):
    queryset = logro.objects.all()
    serializer_class = LogroSerializer
