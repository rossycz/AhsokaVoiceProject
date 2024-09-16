from django.shortcuts import render

# Create your views here.
from AchivementApp.utils import get_random_achievement

def show_random_achievement(request):
    random_achievement = get_random_achievement()
    return render(request,'feed.html', {'logro': random_achievement})