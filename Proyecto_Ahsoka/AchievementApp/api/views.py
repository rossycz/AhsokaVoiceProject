from rest_framework import viewsets
from AchievementApp.models import achievement
from AchievementApp.api.serializer import AchievementSerializer    

class LogroViewSet(viewsets.ModelViewSet):
    queryset = achievement.objects.all()
    serializer_class = AchievementSerializer
