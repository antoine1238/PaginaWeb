
""" django."""
from django.urls import path


""" local."""
from . import views


urlpatterns = [
    path("", views.Home.as_view(), name="tienda"),
    path("add", views.AddProduct.as_view(), name="add"),

]