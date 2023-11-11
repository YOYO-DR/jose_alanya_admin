# Generated by Django 4.1.7 on 2023-11-06 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuesta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuesta',
            name='respuesta',
            field=models.CharField(choices=[('1', 'Nunca'), ('2', 'Casi nunca'), ('3', 'A veces'), ('4', 'Casi siempre'), ('5', 'Siempre')], default='male', max_length=10, verbose_name='Sexo'),
        ),
    ]