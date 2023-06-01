from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    room_id = models.CharField(max_length=64)
    user = models.ManyToManyField(User, verbose_name="ユーザー")


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    message_text = models.CharField(max_length=200)
