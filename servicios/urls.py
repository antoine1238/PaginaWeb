""" django."""
from django.urls import path


""" local."""
from . import views


urlpatterns = [

    path("", views.servicios_home, name = "servicio")
]