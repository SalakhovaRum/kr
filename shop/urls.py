from django.urls import path

from shop.views import create

urlpatterns = [
    path("", create, name='history')
]