from rest_framework import serializers
from AchievementApp.models import achievement 

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = achievement
        fields = '__all__'