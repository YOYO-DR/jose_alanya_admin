# Generated by Django 4.1.7 on 2023-11-02 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictions', '0013_predicteddataprophetresumen'),
    ]

    operations = [
        migrations.AddField(
            model_name='predicteddataprophetresumen',
            name='historic_image',
            field=models.ImageField(blank=True, null=True, upload_to='predicted_images_resumen'),
        ),
    ]
