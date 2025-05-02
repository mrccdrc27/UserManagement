from django.db import models

# Table Test
class Test(models.Model):
    ticketNo = models.CharField(max_length=255)
# Create your models here.
