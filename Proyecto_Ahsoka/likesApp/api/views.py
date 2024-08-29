from rest_framework import generics
from likesApp.models import Likes
from likesApp.api.serializers import LikesSerializer


class LikesListCreate(generics.ListCreateAPIView):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer

class LikesRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer