from rest_framework.routers import DefaultRouter
from likesApp.api.views import LikesViewSet

router = DefaultRouter()
router.register('Likes', LikesViewSet, basename='likes')
urlpatterns = router.urls