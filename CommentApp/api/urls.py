from rest_framework.routers import DefaultRouter
from CommentApp.api.views import CommentViewSet

router =DefaultRouter()
router.register('comments', CommentViewSet, basename='comment')

urlpatterns = router.urls