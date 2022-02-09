from rest_framework import serializers
from .models import Fish


class FishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fish
        fields = ('id', 'name', 'description', 'external_code', 'image')
