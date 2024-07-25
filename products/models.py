from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    video_title = models.CharField(max_length=255, null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
