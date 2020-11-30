""" Django."""
from django.urls import path

""" Local."""
from . import views

urlpatterns = [

    path("", views.PostView.as_view(), name="blog"),
    path("blog_1", views.BlogDetailview.as_view(), name="blog-detail_1"),
    path("blog_2", views.BlogDetailview_2.as_view(), name="blog-detail_2"),
    path("blog_3", views.BlogDetailview_3.as_view(), name="blog-detail_3"),
    path("blog_4", views.BlogDetailview_4.as_view(), name="blog-detail_4"),



]