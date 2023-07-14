from django.urls import path, re_path

from . import views

urlpatterns = [
    path("add_sample_data/", views.add_sample_data),
    re_path(r'^[^/]+', views.fetch_sample_data),
]
