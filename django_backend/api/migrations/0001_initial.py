# Generated by Django 4.1.5 on 2023-01-12 20:27

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DocFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='media')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=200, null=True)),
                ('date', models.CharField(max_length=200, null=True)),
                ('ispolnitelFirmName', models.CharField(max_length=200, null=True)),
                ('ispolnitelDirName', models.CharField(max_length=200, null=True)),
                ('clientFirmName', models.CharField(max_length=200, null=True)),
                ('clientDirName', models.CharField(max_length=200, null=True)),
                ('cargoType', models.CharField(max_length=200, null=True)),
                ('allAdressFrom', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), null=True, size=None)),
                ('allAdressTo', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), null=True, size=None)),
                ('ispOkvedNumber', models.CharField(max_length=6, null=True)),
                ('ispOkvedText', models.CharField(max_length=200, null=True)),
                ('clientOkvedNumber', models.CharField(max_length=6, null=True)),
                ('clientOkvedText', models.CharField(max_length=200, null=True)),
                ('carGrz', models.CharField(max_length=9, null=True)),
                ('carModel', models.CharField(max_length=100, null=True)),
                ('carType', models.CharField(max_length=100, null=True)),
                ('carCargoMin', models.CharField(max_length=20, null=True)),
                ('carCargoMax', models.CharField(max_length=20, null=True)),
                ('carCargo', models.CharField(max_length=20, null=True)),
                ('carCargo80', models.CharField(max_length=20, null=True)),
                ('carCargoMonth', models.CharField(max_length=20, null=True)),
                ('carCargoYear', models.CharField(max_length=20, null=True)),
                ('date_from', models.CharField(max_length=200, null=True)),
                ('date_to', models.CharField(max_length=200, null=True)),
                ('ispolnitelUrAdress', models.CharField(max_length=200, null=True)),
                ('ispolnitelInn', models.CharField(max_length=12, null=True)),
                ('ispolnitelKpp', models.CharField(max_length=200, null=True)),
                ('ispolnitelOgrn', models.CharField(max_length=13, null=True)),
                ('ispolnitelBik', models.CharField(max_length=9, null=True)),
                ('ispolnitelRs', models.CharField(max_length=20, null=True)),
                ('ispolnitelBank', models.CharField(max_length=200, null=True)),
                ('ispolnitelDirShort', models.CharField(max_length=200, null=True)),
                ('clientUrAdress', models.CharField(max_length=200, null=True)),
                ('clientInn', models.CharField(max_length=12, null=True)),
                ('clientKpp', models.CharField(max_length=9, null=True)),
                ('clientOgrn', models.CharField(max_length=13, null=True)),
                ('clientBik', models.CharField(max_length=9, null=True)),
                ('clientRs', models.CharField(max_length=20, null=True)),
                ('clientBank', models.CharField(max_length=200, null=True)),
                ('clientDirShort', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]