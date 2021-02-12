from django.db import models

class Flowchart(models.Model):
    image = models.ImageField(upload_to='images/')
    team = models.CharField(max_length=40)
    date = models.DateTimeField()
