# Generated by Django 4.1.5 on 2023-02-18 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0004_rename_genre_film_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='photo',
            field=models.ImageField(blank=True, upload_to='albumPhoto'),
        ),
    ]
