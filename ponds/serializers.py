from abc import ABC, ABCMeta

from rest_framework import serializers
from .models import Pond, Sector


class SectorListingField(serializers.RelatedField):
    def to_internal_value(self, data):
        pass

    def to_representation(self, value):
        return value.number

    def display_value(self, instance):
        pass

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.order_by('number') if qs else qs


class PondSerializer(serializers.ModelSerializer):
    sectors = SectorListingField(many=True)

    class Meta:
        model = Pond

        fields = ('id', 'name', 'zone', 'width_bottom',
                  'width_top', 'max_depth', 'avg_depth',
                  'square', 'fish_density', 'avg_fish_weight',
                  'description', 'logo', 'address',
                  'sector_width', 'cell_height', 'sectors')


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'

