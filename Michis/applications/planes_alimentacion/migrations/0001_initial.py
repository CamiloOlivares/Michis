# Generated by Django 3.0.5 on 2021-06-08 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('animales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanesAlimentacion',
            fields=[
                ('id_plan_alimentacion', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_inicio', models.DateTimeField()),
                ('observaciones', models.TextField()),
                ('nombre_alimento', models.TextField()),
                ('marca', models.TextField()),
                ('id_animal', models.ForeignKey(db_column='id_animal', on_delete=django.db.models.deletion.DO_NOTHING, to='animales.Animales')),
            ],
            options={
                'db_table': 'planes_alimentacion',
            },
        ),
    ]
