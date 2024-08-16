from rest_framework.routers import DefaultRouter
from ComentarioApp.api.views import ComentarioViewSet

router = DefaultRouter()
router.register('comentarios',ComentarioViewSet, basename='comentario')

urlpatterns = router.urls