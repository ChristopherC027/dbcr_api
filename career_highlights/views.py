from django.shortcuts import render

from rest_framework import generics
from .models import CareerHighlight
from .serializers import CareerHighlightSerializer
from rest_framework.response import Response


class CareerHighlightList(generics.ListCreateAPIView):
    queryset = CareerHighlight.objects.all()
    serializer_class = CareerHighlightSerializer

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        return Response({'results': serializer.data})


class CareerHighlightDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CareerHighlight.objects.all()
    serializer_class = CareerHighlightSerializer

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        return Response({'results': serializer.data})
