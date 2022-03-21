from .views import TournamentViewSet, TournamentTeamViewSet
from rest_framework_nested import routers

router = routers.SimpleRouter()
router.register('tournaments', TournamentViewSet, basename='tournaments')

tournaments_router = routers.NestedSimpleRouter(router, r'tournaments', lookup='tournament')
tournaments_router.register(r'teams', TournamentTeamViewSet, basename='tournament-teams')


urlpatterns = router.urls

