from django.db import models

# Create your models here.
class RegistrosPeso(models.Model):
    
    
    id_animal = models.ForeignKey('animales.animales', models.DO_NOTHING, db_column='id_animal')
    fecha = models.IntegerField(primary_key=True, db_column='fecha')

    peso = models.DateTimeField()
    observaciones = models.TextField()

    class Meta:
        #managed = False
        db_table = 'registros_peso'
        unique_together = (('id_animal', 'fecha'),)