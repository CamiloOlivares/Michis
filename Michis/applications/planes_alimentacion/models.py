from django.db import models

# Create your models here.
class PlanesAlimentacion(models.Model):
    
    id_plan_alimentacion = models.IntegerField(primary_key=True)
    id_animal = models.ForeignKey('animales.Animales', models.DO_NOTHING, db_column='id_animal')

    fecha_inicio = models.DateTimeField()
    observaciones = models.TextField()
    nombre_alimento = models.TextField()
    marca = models.TextField()
   

    class Meta:
        #managed = False
        db_table = 'planes_alimentacion'