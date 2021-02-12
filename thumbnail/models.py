from django.db import models


class Thumbnail(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=40)
    team = models.CharField(max_length=40)
