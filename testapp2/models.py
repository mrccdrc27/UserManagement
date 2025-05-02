from django.db import models

class test3app(models.Model):
    ticketID = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    name2 = models.CharField(max_length=255)
    name3 = models.CharField(max_length=255, null=True)
# Create your models here.
