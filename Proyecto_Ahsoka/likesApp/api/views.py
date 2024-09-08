from rest_framework import generics
from rest_framework import viewsets
from likesApp.models import Likes
from likesApp.api.serializers import LikesSerializer


class LikesListCreate(generics.ListCreateAPIView):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer

class LikesRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer
    
class LikesViewSet(viewsets.ModelViewSet):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer