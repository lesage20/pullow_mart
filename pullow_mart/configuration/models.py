from django.db import models

# Create your models here.


class SocialAccount(models.Model):

    ICONS = {
        ('facebook', "fa-facebook-f"),
        ('instagram', "fa-instagram"),
        ('google-plus', "fa-google-plus-g"),
        ('linkedin', "fa-linkedin-in"),
    }

    nom = models.CharField(max_length=255)
    lien = models.URLField()
    icon = models.CharField(choices=ICONS, max_length=20)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Social Account'
        verbose_name_plural = 'Socials Account'

    def __str__(self):
        return self.nom


class SiteInfo(models.Model):

    map_url = models.TextField()
    email = models.EmailField(max_length=255)
    logo = models.ImageField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Site Info'
        verbose_name_plural = 'Site Infos'

    def __str__(self):
        return self.email


class Presentation(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="images/presentation")
    video = models.URLField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Presentation'
        verbose_name_plural = 'Presentations'

    def __str__(self):
        return self.nom


class Temoignage(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    message = models.TextField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Temoignage'
        verbose_name_plural = 'Temoignages'

    def __str__(self):
        return self.nom
