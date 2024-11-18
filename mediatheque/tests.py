from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import date, timedelta
from bibliothecaire.models import Membre, Media, Emprunt

class EmpruntModelTest(TestCase):

    def setUp(self):
        self.membre = Membre.objects.create(
            nom="Doe",
            prenom="John",
            phone="0746764646",
            email="john.doe@example.com"
        )
        self.livre = Media.objects.create(
            titre="Le Petit Prince",
            auteur_realisateur_artiste="Antoine de Saint-Exupéry",
            type_media="livre"
        )
        self.dvd = Media.objects.create(
            titre="Inception",
            auteur_realisateur_artiste="Christopher Nolan",
            type_media="dvd"
        )
        self.cd = Media.objects.create(
            titre="Thriller",
            auteur_realisateur_artiste="Michael Jackson",
            type_media="cd"
        )
        self.jeu = Media.objects.create(
            titre="Monopoly",
            auteur_realisateur_artiste="Hasbro",
            type_media="jeu"
        )

    def test_emprunt_creation(self):
        emprunt = Emprunt.objects.create(
            media=self.livre,
            emprunteur=self.membre,
            date_emprunt=date.today(),
            date_retour=date.today() + timedelta(days=7)
        )
        self.assertEqual(emprunt.media, self.livre)
        self.assertEqual(emprunt.emprunteur, self.membre)

    def test_emprunt_limite(self):
        # Créez 3 emprunts pour le même membre
        for media in [self.livre, self.dvd, self.cd]:
            Emprunt.objects.create(
                media=media,
                emprunteur=self.membre,
                date_emprunt=date.today(),
                date_retour=date.today() + timedelta(days=7)
            )
        # Tentez de créer un quatrième emprunt
        with self.assertRaises(ValidationError):
            emprunt = Emprunt(
                media=self.jeu,
                emprunteur=self.membre,
                date_emprunt=date.today(),
                date_retour=date.today() + timedelta(days=7)
            )
            emprunt.clean()

    def test_emprunt_retard(self):
        # Créez un emprunt en retard
        emprunt = Emprunt.objects.create(
            media=self.livre,
            emprunteur=self.membre,
            date_emprunt=date.today() - timedelta(days=8),
            date_retour=date.today() - timedelta(days=1)
        )
        # Tentez de créer un nouvel emprunt
        with self.assertRaises(ValidationError):
            nouvel_emprunt = Emprunt(
                media=self.dvd,
                emprunteur=self.membre,
                date_emprunt=date.today(),
                date_retour=date.today() + timedelta(days=7)
            )
            nouvel_emprunt.clean()

    def test_emprunt_jeu_de_plateau(self):
        # Tentez de créer un emprunt pour un jeu de plateau
        with self.assertRaises(ValidationError):
            emprunt = Emprunt(
                media=self.jeu,
                emprunteur=self.membre,
                date_emprunt=date.today(),
                date_retour=date.today() + timedelta(days=7)
            )
            emprunt.clean()


