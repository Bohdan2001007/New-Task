from django.contrib.gis.geos import Point
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Place


class PlaceSerializer(GeoFeatureModelSerializer):
    """
    Серіалізатор для моделі Place. Включає такі поля:
    - 'id': Унікальний ID місця.
    - 'name': Назва місця.
    - 'description': Опис місця.
    - 'geom': Геометричні дані місця у форматі GeoJSON.
    """
    class Meta:
        model = Place
        geo_field = "geom"
        fields = ('id', 'name', 'description', 'geom')

    def create(self, validated_data):
        geom_data = validated_data.pop('geom')
        point = Point(geom_data['coordinates'][0], geom_data['coordinates'][1])
        place = Place.objects.create(geom=point, **validated_data)
        return place
