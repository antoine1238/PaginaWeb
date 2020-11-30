
""" django."""
from django.urls import path


""" local."""
from . import views


urlpatterns = [

    path("login/", views.Login.as_view() , name = "login"),
    path("logout/", views.Logout.as_view() , name = "logout"),
    path("signup/", views.Signup , name = "signup"),
    path("update/", views.UpdateProfile.as_view() , name = "update"),
    path("", views.home.as_view(), name="home"),
    path('<str:username>/', views.Detail.as_view(), name = 'detail'),
    

]