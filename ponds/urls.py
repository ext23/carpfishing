from rest_framework.routers import SimpleRouter
from .views import PondViewSet

router = SimpleRouter()
router.register('ponds', PondViewSet, basename='ponds')

urlpatterns = router.urls
