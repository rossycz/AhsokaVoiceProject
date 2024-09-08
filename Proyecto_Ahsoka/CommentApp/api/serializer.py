from rest_framework import serializers
from CommentApp.models import comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=comment
        fields='__all__'
        
