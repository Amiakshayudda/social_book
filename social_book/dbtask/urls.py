from django.urls import path

from . import views

urlpatterns = [
    path("fetchall", views.fetchall, name="fetchall"),
    path("uploadbooks", views.uploadbooks, name="uploadbooks"),
    path("viewbooks", views.viewbooks, name="viewbooks")
]
