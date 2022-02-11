from rest_framework import viewsets

from .models import Person, Member, Judge
from .serializers import PersonSerializer, MemberSerializer, JudgeSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class JudgeViewSet(viewsets.ModelViewSet):
    queryset = Judge.objects.all()
    serializer_class = JudgeSerializer
