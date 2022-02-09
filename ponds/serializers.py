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

        fields = ('id', 'name', 'zone', 'width_bottom', 'width_top',
                  'max_depth', 'avg_depth', 'square', 'fish_density',
                  'avg_fish_weight', 'description', 'logo', 'address',
                  'width', 'sector_width', 'cell_height', 'sectors')


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = ('pond', 'number')