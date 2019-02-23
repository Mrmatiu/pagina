# Generated by Django 2.1.2 on 2018-12-04 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20181204_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservacion',
            name='camisa',
            field=models.CharField(choices=[('Negra', 'Negra'), ('Blanca', 'Blanca')], max_length=2),
        ),
        migrations.AlterField(
            model_name='reservacion',
            name='corbata',
            field=models.CharField(choices=[('Azul', 'Azul'), ('Verde', 'Verde'), ('Rojo', 'Rojo')], max_length=2),
        ),
        migrations.AlterField(
            model_name='reservacion',
            name='modelo',
            field=models.CharField(choices=[('Tuxedo', 'Tuxedo'), ('Slim Fit', 'Slim fit'), ('Clasico', 'Clasico')], max_length=2),
        ),
    ]