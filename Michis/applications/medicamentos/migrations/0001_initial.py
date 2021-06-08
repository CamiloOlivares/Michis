# Generated by Django 3.0.5 on 2021-06-08 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tratamientos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicamentos',
            fields=[
                ('id_medicamento', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_termino', models.DateTimeField()),
                ('nombre_medicamento', models.TextField()),
                ('dosis', models.TextField()),
                ('observaciones', models.TextField()),
                ('id_tratamiento', models.ForeignKey(db_column='id_tratamiento', on_delete=django.db.models.deletion.DO_NOTHING, to='tratamientos.Tratamientos')),
            ],
            options={
                'db_table': 'medicamentos',
            },
        ),
    ]
