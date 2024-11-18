# Generated by Django 5.1.2 on 2024-11-11 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliothecaire', '0002_membre_email_membre_prenom_alter_membre_bloque'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='date_emprunt',
        ),
        migrations.RemoveField(
            model_name='media',
            name='emprunteur',
        ),
        migrations.AddField(
            model_name='media',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media_images/'),
        ),
    ]
