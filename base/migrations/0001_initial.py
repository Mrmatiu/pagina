# Generated by Django 2.1.2 on 2018-12-02 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128)),
                ('apellido', models.CharField(max_length=128)),
                ('telefono', models.DecimalField(decimal_places=0, max_digits=20)),
                ('pecho', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1)),
                ('cintura', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1)),
                ('largo', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1)),
                ('manga', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1)),
                ('cuello', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='reservacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monio', models.CharField(choices=[('Si', 'Si'), ('No', 'No')], max_length=2)),
                ('camisa', models.CharField(choices=[('N', 'Negra'), ('B', 'Blanca')], max_length=2)),
                ('corbata', models.CharField(choices=[('A', 'Azul'), ('V', 'Verde'), ('R', 'Rojo')], max_length=2)),
                ('modelo', models.CharField(choices=[('T', 'Tuxedo'), ('SL', 'Slim fit'), ('C', 'Clasico')], max_length=2)),
                ('costo', models.DecimalField(decimal_places=4, max_digits=20)),
                ('anticipo', models.DecimalField(decimal_places=4, max_digits=20)),
                ('saldo', models.DecimalField(decimal_places=4, max_digits=20)),
                ('deposito', models.DecimalField(decimal_places=4, max_digits=20)),
                ('registro', models.DateTimeField(auto_now_add=True)),
                ('entrega', models.DateField()),
                ('devolucion', models.DateField()),
                ('clienteid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.cliente')),
            ],
        ),
    ]
