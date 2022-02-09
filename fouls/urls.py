from rest_framework.routers import SimpleRouter
from .views import FoulViewSet

router = SimpleRouter()
router.register('fouls', FoulViewSet, basename='fouls')

urlpatterns = router.urls
