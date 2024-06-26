from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("classifications/", views.classifications, name="classifications"),
]