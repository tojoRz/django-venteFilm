from django.db import models

# Create your models here.

class  Genre(models.Model):
    name = models.CharField('Nom',max_length=200, unique=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "genre"


class Contact(models.Model):
    email = models.EmailField('Email',max_length=100)
    nom = models.CharField('Nom',max_length=200)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "contact"

class Film(models.Model):
    reference = models.IntegerField('Référence',null=True)
    create_at = models.DateTimeField('Date de création',auto_now_add=True)
    disponible = models.BooleanField('Disponible',default=True)
    titre = models.CharField('Titre',max_length=300)
    photo = models.ImageField("URL de l'image",upload_to= "albumPhoto", blank=True, null=False)
    genres = models.ManyToManyField(Genre, related_name='film', blank=True)

    def __str__(self):
        return self.titre

    class Meta:
        verbose_name = "film"

class Reservation(models.Model):
    create_at = models.DateTimeField("Date d'envoi",auto_now_add=True)
    contacted = models.BooleanField('Demande traitée ?',default=False)
    contact = models.ForeignKey("Contact", on_delete=models.CASCADE)
    film = models.OneToOneField("Film", on_delete=models.PROTECT)
     
    def __str__(self):
        return self.contact.nom

    class Meta:
        verbose_name = "réservation"    