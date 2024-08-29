from rest_framework.routers import DefaultRouter
from LogroApp.api.views import LogroViewSet

router = DefaultRouter()
router.register('Likes', LogroViewSet, basename='likes')
urlpatterns = router.urls