from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='profileimage')