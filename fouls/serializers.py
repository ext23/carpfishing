from rest_framework import serializers
from .models import Foul


class FoulSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foul
        fields = ('id', 'name', 'external_code', 'decision')
