# bibliothecaire/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('accueil/liste_membres/', views.membre_list, name='liste_membres'),
    path('accueil/liste_medias/', views.media_list, name='liste_medias'),
    path('accueil/liste_emprunt/', views.emprunt_list, name='liste_emprunt'),
    path('accueil/', views.accueil, name='accueil')
]

