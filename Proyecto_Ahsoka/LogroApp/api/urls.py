from rest_framework.routers import DefaultRouter
from LogroApp.api.views import LogroViewSet

router = DefaultRouter()
router.register('Logros', LogroViewSet, basename='logro')
urlpatterns = router.urls