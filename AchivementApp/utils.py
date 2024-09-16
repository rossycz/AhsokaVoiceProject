#utils
from django.db.models import F, Func
from AchivementApp.models import Achievement

def get_random_achievement(): 
    # Obtiene un objeto aleatorio usando PostgreSQL
    random_achievement = Achievement.objects.order_by(Func(function='RANDOM')).first()
    return random_achievement
