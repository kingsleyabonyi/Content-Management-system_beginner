from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Userprofiles(models.Model):
    user = models.OneToOneField( User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=100)
    profession = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='img', blank=True, null=True)
    about = models.TextField(max_length=400)
    profile_id = models.BigIntegerField()


    def __str__(self):
        return self.username
