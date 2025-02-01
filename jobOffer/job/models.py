from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    pp= models.ImageField(upload_to=("directory_image/"))
    user= models.OneToOneField(User, on_delete=models.CASCADE)
