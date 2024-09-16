from django.urls import path, include
from UserApp.views import index_us

app_name = 'user'

urlpatterns = [

    path('/index',index_us),
     
]

