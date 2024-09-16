from rest_framework import viewsets
from CommentApp.models import Comment
from CommentApp.api.serializer import CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer