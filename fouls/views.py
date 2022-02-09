from rest_framework import viewsets

from .models import Foul
from .serializers import FoulSerializer


class FoulViewSet(viewsets.ModelViewSet):
    queryset = Foul.objects.all()
    serializer_class = FoulSerializer
