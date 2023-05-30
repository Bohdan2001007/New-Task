from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import Place
from .serializers import PlaceSerializer


class PlacesListView(ListAPIView):
    """
    Список усіх місць. Повертає список усіх місць в базі даних.
    """
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class CreatePlaceView(CreateAPIView):
    """
    Створення нового місця. Приймає дані у форматі JSON і створює нове місце в базі даних.
    """
    serializer_class = PlaceSerializer


class UpdatePlaceView(UpdateAPIView):
    """
    Оновлення існуючого місця. Приймає ID місця і дані у форматі JSON для оновлення місця.
    """
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class DeletePlaceView(DestroyAPIView):
    """
    Видалення місця. Приймає ID місця, яке потрібно видалити.
    """
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class NearestPlaceView(ListAPIView):
    """
    Пошук найближчого місця. Приймає координати (широту і довготу) і повертає найближче місце.
    """
    serializer_class = PlaceSerializer

    def get_queryset(self):
        latitude = self.kwargs['latitude']
        longitude = self.kwargs['longitude']
        user_location = Point(latitude, longitude, srid=4326)
        nearest_place = Place.objects.annotate(distance=Distance('geom', user_location)).order_by('distance')[:1]
        return nearest_place
