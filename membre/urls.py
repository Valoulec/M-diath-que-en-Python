# membre/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.media_list, name='media_list'),
    path('media/<int:media_id>/', views.media_detail, name='media_detail'),
]
