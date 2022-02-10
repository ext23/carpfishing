from rest_framework.routers import SimpleRouter
from .views import PersonViewSet

router = SimpleRouter()
router.register('persons', PersonViewSet, basename='persons')

urlpatterns = router.urls
