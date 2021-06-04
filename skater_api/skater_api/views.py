from rest_framework import generics
from .serializers import SkaterSerializer, TricksSerializer
from .models import Skater, Tricks

class SkaterList(generics.ListCreateAPIView):
    queryset = Skater.objects.all()
    serializer_class = SkaterSerializer

class SkaterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skater.objects.all()
    serializer_class = SkaterSerializer

class TricksList(generics.ListCreateAPIView):
    queryset = Tricks.objects.all()
    serializer_class = TricksSerializer

class TricksDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tricks.objects.all()
    serializer_class = TricksSerializer

