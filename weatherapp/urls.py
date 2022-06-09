from .views import TemperatureView
from django.urls import path

urlpatterns = [
    path('',TemperatureView.as_view(),name="city_temp"),
]