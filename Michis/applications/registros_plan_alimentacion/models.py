from django.db import models

# Create your models here.
class RegistrosPlanAlimentacion(models.Model):
    
    #**ver como hacer clave compuesta
    id_plan_alimentacion = models.ForeignKey('animales.Animales', models.DO_NOTHING, db_column='id_animal')
    fecha = models.IntegerField(primary_key=True)

    id_cuidador = models.ForeignKey('cuidadores.Cuidadores', models.DO_NOTHING, db_column='id_cuidador')
    observaciones = models.TextField()

   

    class Meta:
        #managed = False
        db_table = 'registros_plan_alimentacion'