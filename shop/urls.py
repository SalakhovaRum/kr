from django.urls import path
from .views import calculate_view, conclusion_view

urlpatterns = [
    path("calculate", calculate_view, name='calculate'),
    path('conclusion', conclusion_view, name='conclusion'),
]