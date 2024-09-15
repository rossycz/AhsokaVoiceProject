from rest_framework import viewsets
from UserApp.models import User
from UserApp.api.serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class = UserSerializer
