from django.db import models

# Create your models here.
class Animales(models.Model):
    id_animal = models.AutoField(primary_key=True)
    nombre = models.TextField()
    especie = models.TextField()  
    raza = models.TextField()
    sexo = models.TextField()
    esterilizado =  models.BooleanField(default=False)
    color = models.TextField()
    fecha_nacimiento = models.DateTimeField()
    observaciones = models.TextField()
    

    class Meta:
        #managed = False
        verbose_name = 'Animal'
        verbose_name_plural = 'Animales'
        db_table = 'animales'