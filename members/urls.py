from rest_framework.routers import SimpleRouter
from .views import MemberViewSet

router = SimpleRouter()
router.register('members', MemberViewSet, basename='members')

urlpatterns = router.urls
