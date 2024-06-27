from django.urls import path

from . import views, api

urlpatterns = [
    path("", views.index, name="index"),
    path("classifications/", views.classifications, name="classifications"),
    path("table/", views.table, name="table"),
    path('api/get_leagues/', api.get_leagues, name='get_leagues'),
    path('api/get_teams/<int:league_id>/', api.get_teams, name='get_teams'),
]