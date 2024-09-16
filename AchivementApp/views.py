from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from AchivementApp.utils import get_random_achievement

def index_achievement(request):
    return HttpResponse("Index")

#def logros_list(request):
 #   logro=Achievement.objects.all()
  #  contexto ={'logros':logro}
   # return render(request,'logros_list.html',contexto)

def show_random_achievement(request):
    random_achievement = get_random_achievement()
    return render(request,'feed.html', {'achievement': random_achievement})

