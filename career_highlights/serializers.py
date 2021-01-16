from rest_framework import serializers
from .models import CareerHighlight


class CareerHighlightSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        fields = ('id', 'image', 'name', 'website')
        model = CareerHighlight
