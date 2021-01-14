from rest_framework import serializers
from .models import ArticleHighlight


class ArticleHighlightSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        fields = ('id', 'image', 'name', 'website')
        model = ArticleHighlight
