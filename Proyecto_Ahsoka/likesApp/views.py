from rest_framework import generics
from .models import Likes
from .serializers import LikesSerializer


class LikesListCreate(generics.ListCreateAPIView):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer

class BookRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer