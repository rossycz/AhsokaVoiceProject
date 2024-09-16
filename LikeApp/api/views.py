from rest_framework import viewsets
from LikeApp.models import Like
from LikeApp.api.serializer import LikeSerializer

class LikeViewSet(viewsets.ModelViewSet):
    queryset=Like.objects.all()
    serializer_class=LikeSerializer
    