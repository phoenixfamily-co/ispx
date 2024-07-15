from django.db import models


# Create your models here.
class Slider(models.Model):
    Image = models.ImageField()
    Title = models.CharField(max_length=255)


class CEO(models.Model):
    Title = models.CharField(max_length=255)
    Image = models.ImageField()
    Description = models.TextField()
