from rest_framework import viewsets
from CommentApp.models import comment
from CommentApp.api.serializer import CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = comment.objects.all()
    serializer_class = CommentSerializer
    