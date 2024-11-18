# Generated by Django 5.1.2 on 2024-11-09 14:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Membre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('bloque', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('auteur_realisateur_artiste', models.CharField(max_length=100)),
                ('type_media', models.CharField(choices=[('livre', 'Livre'), ('dvd', 'DVD'), ('cd', 'CD'), ('jeu', 'Jeu de Plateau')], max_length=10)),
                ('disponible', models.BooleanField(default=True)),
                ('date_emprunt', models.DateField(blank=True, null=True)),
                ('emprunteur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bibliothecaire.membre')),
            ],
        ),
        migrations.CreateModel(
            name='Emprunt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_emprunt', models.DateField(auto_now_add=True)),
                ('date_retour', models.DateField(blank=True, null=True)),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bibliothecaire.media')),
                ('emprunteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bibliothecaire.membre')),
            ],
        ),
    ]