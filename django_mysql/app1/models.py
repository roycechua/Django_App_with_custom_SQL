from django.db import models

# Create your models here.
class Students(models.Model):
    first_name = models.CharField(max_length=255)