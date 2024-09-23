from django.urls import path
from .views import get_walking_data, get_bicycle_data, get_carshare_data

urlpatterns = [
    path('walking/', get_walking_data, name='get_walking_data'),
    path('bicycle/', get_bicycle_data, name='get_bicycle_data'),
    path('carshare/', get_carshare_data, name='get_carshare_data'),
]
