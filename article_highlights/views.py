from django.shortcuts import render

from rest_framework import generics
from .models import ArticleHighlight
from .serializers import ArticleHighlightSerializer
from rest_framework.response import Response


class ArticleHighlightList(generics.ListCreateAPIView):
    queryset = ArticleHighlight.objects.all()
    serializer_class = ArticleHighlightSerializer

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        return Response({'results': serializer.data})


class ArticleHighlightDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ArticleHighlight.objects.all()
    serializer_class = ArticleHighlightSerializer

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        return Response({'results': serializer.data})
