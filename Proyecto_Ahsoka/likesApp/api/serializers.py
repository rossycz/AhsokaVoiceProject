from rest_framework import serializers
from likesApp.models import Likes

class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = '__all__'