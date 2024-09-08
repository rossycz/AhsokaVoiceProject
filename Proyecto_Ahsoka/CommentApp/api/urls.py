from rest_framework.routers import DefaultRouter
from CommentApp.api.views import CommentViewSet

router = DefaultRouter()
router.register('comentarios',CommentViewSet, basename='comentario')

urlpatterns = router.urls