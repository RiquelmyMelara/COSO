# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Componente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('peso', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='COSO',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Enfoque',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('peso', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Enunciados',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('peso', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Principio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('peso', models.IntegerField()),
                ('componente', models.ForeignKey(to='CosoApp.Componente')),
            ],
        ),
        migrations.AddField(
            model_name='enunciados',
            name='principio',
            field=models.ForeignKey(to='CosoApp.Principio'),
        ),
        migrations.AddField(
            model_name='enfoque',
            name='principio',
            field=models.ForeignKey(to='CosoApp.Principio'),
        ),
        migrations.AddField(
            model_name='componente',
            name='coso',
            field=models.ForeignKey(to='CosoApp.COSO'),
        ),
    ]
