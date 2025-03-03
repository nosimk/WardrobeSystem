from django.db import models

# Create your models here.
class Wardrobe(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    season = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    def __str__(self):
        return self.name
