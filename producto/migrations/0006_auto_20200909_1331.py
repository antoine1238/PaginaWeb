# Generated by Django 3.0.8 on 2020-09-09 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0005_producto_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=240),
        ),
    ]
