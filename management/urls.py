from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.register),
    path('show', views.show),
    path('send', views.send),
    path('delete', views.delete),
    path('edit', views.edit),
    path('RecordEdited', views.RecordEdited)
]