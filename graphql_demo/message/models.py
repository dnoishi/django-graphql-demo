from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Message(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    creation_date = models.DateTimeField(auto_now_add=True)
    message = models.TextField()