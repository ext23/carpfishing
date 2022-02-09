from rest_framework import viewsets

from .models import Pond, Sector
from .serializers import PondSerializer, SectorSerializer


class PondViewSet(viewsets.ModelViewSet):
    queryset = Pond.objects.all()
    serializer_class = PondSerializer


class SectorViewSet(viewsets.ModelViewSet):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer
