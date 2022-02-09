from rest_framework.routers import SimpleRouter
from .views import PondViewSet, SectorViewSet

router = SimpleRouter()
router.register('ponds', PondViewSet, basename='ponds')
router.register('sectors', SectorViewSet, basename='sectors')

urlpatterns = router.urls
