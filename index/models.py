from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Room(models.Model):

    name = models.CharField(max_length=100, unique=True)
    users = models.ManyToManyField(User, blank=True, related_name='user')
    secretcode = models.CharField(max_length=100)



class Masseages(models.Model):

    text = models.CharField(max_length=3000)

    date = models.DateTimeField()

    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='masseages')

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')