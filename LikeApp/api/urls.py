from rest_framework.routers import DefaultRouter
from LikeApp.api.views import LikeViewSet

router = DefaultRouter()
router.register('likes',LikeViewSet,basename='like')
urlpatterns = router.urls
