from distutils.command.upload import upload
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    id_no = models.IntegerField()
    img_profile = models.ImageField(upload_to='images/')
