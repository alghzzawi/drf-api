from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import CoffeeSerializer
from .models import Coffee
# Create your views here.

class CoffeeListView(ListAPIView):
    queryset=Coffee.objects.all()
    serializer_class=CoffeeSerializer

class CoffeeDetailView(RetrieveAPIView):
    queryset=Coffee.objects.all()
    serializer_class=CoffeeSerializer

class CoffeeUpdateView(RetrieveUpdateAPIView):
    queryset=Coffee.objects.all()
    serializer_class=CoffeeSerializer

class CoffeeDeleteView(RetrieveUpdateDestroyAPIView):
    queryset=Coffee.objects.all()
    serializer_class=CoffeeSerializer

class CoffeeCreateView(ListCreateAPIView):
    queryset=Coffee.objects.all()
    serializer_class=CoffeeSerializer