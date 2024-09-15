from rest_framework import serializers
from AchivementApp.models import Achievement

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'

