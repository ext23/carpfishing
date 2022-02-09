from rest_framework.routers import SimpleRouter
from .views import FishViewSet

router = SimpleRouter()
router.register('fishes', FishViewSet, basename='fishes')

urlpatterns = router.urls
