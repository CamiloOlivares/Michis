from django.db import models

# Create your models here.
class Cuidadores(models.Model):
    
    id_cuidador = models.IntegerField(primary_key=True)
    
    fecha_ingreso = models.DateTimeField()
    nombre = models.TextField()

    class Meta:
        #managed = False
        verbose_name = 'Cuidador'
        verbose_name_plural = 'Cuidadores'
        db_table = 'cuidadores'