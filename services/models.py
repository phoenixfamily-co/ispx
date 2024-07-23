from django.db import models


# Create your models here.

class Services(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)
