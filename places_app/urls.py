from django.urls import path
from .views import PlacesListView, CreatePlaceView, UpdatePlaceView, DeletePlaceView, NearestPlaceView
from django.urls import register_converter


class FloatConverter:
    regex = '[+-]?([0-9]*[.])?[0-9]+'

    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return str(value)


register_converter(FloatConverter, 'float')

urlpatterns = [
    path('', PlacesListView.as_view(), name='places_list'),
    path('create/', CreatePlaceView.as_view(), name='create_place'),
    path('update/<int:pk>/', UpdatePlaceView.as_view(), name='update_place'),
    path('delete/<int:pk>/', DeletePlaceView.as_view(), name='delete_place'),
    path('nearest/<float:latitude>/<float:longitude>/', NearestPlaceView.as_view(), name='nearest_place'),
]
