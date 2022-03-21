from django.urls import path

from . import views


app_name = 'API'
urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('notes', views.getNotes, name="notes"),
]
