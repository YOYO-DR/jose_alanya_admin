# Generated by Django 4.1.7 on 2023-11-02 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictions', '0010_predicteddataforpublicacionesfacebook_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='predicteddataforpublicacionesfacebook',
            name='publications',
            field=models.ManyToManyField(to='predictions.publicacionesfacebook'),
        ),
    ]
