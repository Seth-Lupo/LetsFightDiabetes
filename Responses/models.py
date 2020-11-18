from django.db import models

# Create your models here.

class Response (models.Model):

    article = models.CharField(max_length=1)
    name = models.CharField(max_length=30)
    content = models.CharField(max_length=500)

