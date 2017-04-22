# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-22 20:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvanceProtocoloExperimentoProyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Contenedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Experimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ExperimentoProtocolo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('experimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laboratorio.Experimento')),
            ],
        ),
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('unidad', models.CharField(choices=[('mg', 'Miligramo'), ('gr', 'Gramo'), ('Kg', 'Kilogramo'), ('ml', 'Mililitro'), ('Lt', 'Litro')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=4, default=0, max_digits=10)),
                ('contenedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laboratorio.Contenedor')),
                ('insumo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laboratorio.Insumo')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('estado', models.CharField(choices=[('G', 'Generada'), ('P', 'Proceso'), ('T', 'Terminada'), ('C', 'Cancelada')], max_length=1)),
                ('cantidad', models.DecimalField(decimal_places=4, default=0, max_digits=10)),
                ('insumo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laboratorio.Insumo')),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.Group')),
                ('descripcion', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Perfiles',
            },
            bases=('auth.group',),
        ),
        migrations.CreateModel(
            name='Protocolo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('nit', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProyectoExperimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('experimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laboratorio.Experimento')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laboratorio.Proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('perfil', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='laboratorio.Perfil')),
            ],
        ),
        migrations.CreateModel(
            name='VersionProtocolo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('protocolo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laboratorio.Protocolo')),
            ],
        ),
        migrations.AddField(
            model_name='experimentoprotocolo',
            name='protocolo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laboratorio.Protocolo'),
        ),
        migrations.AddField(
            model_name='avanceprotocoloexperimentoproyecto',
            name='proy_experimento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laboratorio.ProyectoExperimento'),
        ),
    ]
