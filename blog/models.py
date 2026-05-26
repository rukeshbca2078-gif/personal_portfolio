from django.db import models

class blog (models.Model):
    name = models.CharField(max_length=100)
