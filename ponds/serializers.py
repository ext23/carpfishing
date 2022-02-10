from rest_framework import serializers
from .models import Pond, Sector


class PondSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pond
        sectors = serializers.SlugRelatedField(
            many=True,
            read_only=True,
            slug_field='number',
            allow_null=True,
            required=False)

        fields = ('__all__')


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = ('__all__')