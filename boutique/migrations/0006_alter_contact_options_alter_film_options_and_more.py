# Generated by Django 4.1.5 on 2023-02-18 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0005_alter_film_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'contact'},
        ),
        migrations.AlterModelOptions(
            name='film',
            options={'verbose_name': 'film'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'genre'},
        ),
        migrations.AlterModelOptions(
            name='reservation',
            options={'verbose_name': 'réservation'},
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=100, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='nom',
            field=models.CharField(max_length=200, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='film',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='film',
            name='disponible',
            field=models.BooleanField(default=True, verbose_name='Disponible'),
        ),
        migrations.AlterField(
            model_name='film',
            name='photo',
            field=models.ImageField(blank=True, upload_to='albumPhoto', verbose_name="URL de l'image"),
        ),
        migrations.AlterField(
            model_name='film',
            name='reference',
            field=models.IntegerField(null=True, verbose_name='Référence'),
        ),
        migrations.AlterField(
            model_name='film',
            name='titre',
            field=models.CharField(max_length=300, verbose_name='Titre'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='contacted',
            field=models.BooleanField(default=False, verbose_name='Demande traitée ?'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name="Date d'envoi"),
        ),
    ]
