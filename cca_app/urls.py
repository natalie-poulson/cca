from django.urls import path
from . import views

urlpatterns = [
    path('api/sections', views.api, name='api'),
]