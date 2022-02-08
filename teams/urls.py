from rest_framework.routers import SimpleRouter
from .views import TeamViewSet

router = SimpleRouter()
router.register('teams', TeamViewSet, basename='teams')

urlpatterns = router.urls
