# Generated by Django 5.1.2 on 2024-11-11 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliothecaire', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='membre',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='membre',
            name='prenom',
            field=models.CharField(default='DefaultPrenom', max_length=100),
        ),
        migrations.AlterField(
            model_name='membre',
            name='bloque',
            field=models.CharField(max_length=100),
        ),
    ]