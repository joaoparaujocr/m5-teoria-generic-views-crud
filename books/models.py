from django.db import models

class Book(models.Model):
    pages = models.IntegerField()
    title = models.CharField(max_length=255)
    