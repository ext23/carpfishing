from rest_framework import serializers
from .models import Member


class MemberSerializer(serializers.ModelSerializer):
    captain_of_team = serializers.CharField(source='captain_team', read_only=True)
    assistant_of_team = serializers.CharField(source='assistant_team', read_only=True)

    class Meta:
        model = Member
        fields = ('__all__')
