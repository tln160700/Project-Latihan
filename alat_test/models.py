from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.
class SoalCPM (models.Model):
    KalimatSoal = models.CharField(max_length=8, default="")
    GambarSoal = models.ImageField(upload_to = 'CPM/Soal')

class JawabanCPM (models.Model):
    KalimatJawaban = models.CharField(max_length=8, default="")
    GambarJawaban = models.ImageField(upload_to = 'CPM/Jawaban')
    KonektorJawaban = models.ForeignKey(SoalCPM, on_delete=models.CASCADE)
