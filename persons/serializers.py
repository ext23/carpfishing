from rest_framework import serializers
from .models import Person, Member, Judge


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='person.first_name', read_only=True)
    last_name = serializers.CharField(source='person.last_name', read_only=True)
    captain_of_team = serializers.CharField(source='captain_team', read_only=True)
    assistant_of_team = serializers.CharField(source='assistant_team', read_only=True)

    class Meta:
        model = Member
        fields = '__all__'


class JudgeSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='person.first_name', read_only=True)
    last_name = serializers.CharField(source='person.last_name', read_only=True)

    class Meta:
        model = Judge
        fields = '__all__'
