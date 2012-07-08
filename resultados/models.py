from django.db import models

class Resultado(models.Model):
    data = models.DateField()
    TURNOS = (
        ('1','Noturno'),
        ('2','Diurno'),
    )
    turno = models.CharField(max_length=1, choices=TURNOS)
    premio_1 = models.IntegerField(max_length=4)
    premio_2 = models.IntegerField(max_length=4)
    premio_3 = models.IntegerField(max_length=4)
    premio_4 = models.IntegerField(max_length=4)
    premio_5 = models.IntegerField(max_length=4)
    premio_6 = models.IntegerField(max_length=4)
    premio_7 = models.IntegerField(max_length=4)
    premio_8 = models.IntegerField(max_length=4)
    premio_9 = models.IntegerField(max_length=4)
    premio_10 = models.IntegerField(max_length=4)    
