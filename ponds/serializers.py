from rest_framework import serializers
from .models import Pond


class PondSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pond
        fields = ('id', 'name', 'zone', 'width_bottom', 'width_top',
                  'max_depth', 'avg_depth', 'square', 'fish_density',
                  'avg_fish_weight', 'description', 'logo', 'address',
                  'width', 'sector_width', 'cell_height')
