# Generated by Django 2.1.2 on 2018-12-04 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_reservacion_entregado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservacion',
            name='entregado',
            field=models.CharField(choices=[('Si', 'Si'), ('No', 'No')], default='No', max_length=2),
        ),
    ]