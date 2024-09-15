from rest_framework.routers import DefaultRouter
from UserApp.api.views import UserViewSet

router = DefaultRouter()
router.register('users',UserViewSet, basename='user')
urlpatterns = router.urls