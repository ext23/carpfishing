from rest_framework.routers import SimpleRouter
from .views import PersonViewSet, MemberViewSet, JudgeViewSet

router = SimpleRouter()
router.register('persons', PersonViewSet, basename='persons')
router.register('members', MemberViewSet, basename='members')
router.register('judges', JudgeViewSet, basename='judges')

urlpatterns = router.urls
