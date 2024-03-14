
from django.db import models

class SensorData(models.Model):
    Sensor = models.BooleanField()
    Botao = models.BooleanField()
    LigaRobo = models.BooleanField()
    ResetContador = models.BooleanField()
    Valor_Contagem = models.IntegerField()