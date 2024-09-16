
from AchivementApp.views import index_achievement
from django.urls import path, include

app_name = 'achievement'

urlpatterns = [
    path('/index',index_achievement),
]

