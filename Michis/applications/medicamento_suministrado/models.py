from django.db import models

# Create your models here.
class MedicamentoSuministrado(models.Model):
    
    id_medicamento = models.IntegerField(primary_key=True)
    id_tratamiento = models.ForeignKey('tratamientos.Tratamientos', models.DO_NOTHING, db_column='id_tratamiento')

    id_cuidador = models.ForeignKey('cuidadores.Cuidadores', models.DO_NOTHING, db_column='id_cuidador')

    fecha = models.DateTimeField()
    
    nombre_medicamento = models.TextField()
    dosis = models.TextField()
    observaciones = models.TextField()

    class Meta:
        #managed = False
        db_table = 'medicamento_suministrado'