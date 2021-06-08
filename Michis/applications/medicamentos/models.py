from django.db import models

# Create your models here.
class Medicamentos(models.Model):
    
    id_medicamento = models.IntegerField(primary_key=True)
    id_tratamiento = models.ForeignKey('tratamientos.Tratamientos', models.DO_NOTHING, db_column='id_tratamiento')

    fecha_inicio = models.DateTimeField()
    fecha_termino = models.DateTimeField()
    
    nombre_medicamento = models.TextField()
    dosis = models.TextField()
    observaciones = models.TextField()

    class Meta:
        #managed = False
        db_table = 'medicamentos'
