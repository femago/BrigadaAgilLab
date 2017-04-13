# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 20:09
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
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('perfil', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='laboratorio.Perfil')),
            ],
        ),
    ]