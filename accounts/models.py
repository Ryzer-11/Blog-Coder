from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatars', null=True, blank=True)


#class Familia(models.Model):
    #parentesco= models.CharField(max_length=30)
    #nombre= models.CharField(max_length=30)
    #edad= models.IntegerField()
    #fechaDeNacimiento= models.DateField()    