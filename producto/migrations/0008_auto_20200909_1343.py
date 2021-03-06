# Generated by Django 3.0.8 on 2020-09-09 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0007_remove_producto_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(blank=True, max_length=240),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='tienda'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
