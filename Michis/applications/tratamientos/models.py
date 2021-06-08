from django.db import models

# Create your models here.
class Tratamientos(models.Model):
    
    id_tratamiento = models.IntegerField(primary_key=True)
    id_animales = models.ForeignKey('animales.Animales', models.DO_NOTHING, db_column='id_animal')

    nombre = models.TextField()
    fecha = models.DateTimeField()
    observaciones = models.TextField()

    class Meta:
        #managed = False
        db_table = 'tratamientos'
