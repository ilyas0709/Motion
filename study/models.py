from django.db import models


class Icons(models.Model):
    icons = models.ImageField(upload_to='icon/')


class Images(models.Model):
    images = models.ImageField(upload_to='image/')


class Videos(models.Model):
    urls = models.URLField(max_length=200)

    def __str__(self):
        return self.urls


class Texts(models.Model):
    texts = models.TextField()

    def __str__(self):
        return self.texts





# class Photos(models.Model):
#     photo = models.ImageField(upload_to='photo/')


# Create your models here.
