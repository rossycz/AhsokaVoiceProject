from rest_framework import serializers
from ComentarioApp.models import comentario

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=comentario
        fields='__all__'
        
