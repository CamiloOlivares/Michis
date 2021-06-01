from django.db import models

# Create your models here.


class Animales(models.Model):

    animal_choices = (
        ('0', 'Perro'),
        ('1', 'Gato'),
        ('2', 'Otro'),
    )

    sexo_choices = (
        ('0', 'Macho'),
        ('1', 'Hembra'),
        ('2', 'Otro'),
    )

    nombre = models.CharField('Nombre', max_length=50)
    tipo = models.CharField('Tipo', max_length=1, choices=animal_choices)
    raza = models.CharField('Raza', max_length=50)
    sexo = models.CharField('Sexo', max_length=1, choices=sexo_choices)
    castrado = models.BooleanField('Castrado', default=False)
    color = models.CharField('Color', max_length=50)
    fecha_nacimiento = models.DateField(
        "Fecha de Nac", auto_now=False, auto_now_add=False)
    observaciones = models.CharField("Observaciones", max_length=50)

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animales'

    def __str__(self):
        return self.nombre
