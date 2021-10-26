from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.
class SoalCPM (models.Model):
    label = models.CharField(max_length=8, default="")
    

class JawabanCPM (models.Model):
    label = models.CharField(max_length=8, default="")

