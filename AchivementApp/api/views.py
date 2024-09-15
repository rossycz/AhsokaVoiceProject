from rest_framework import viewsets
from AchivementApp.models import Achievement
from AchivementApp.api.serializer import AchievementSerializer

class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.filter(status=True) 
    serializer_class =AchievementSerializer