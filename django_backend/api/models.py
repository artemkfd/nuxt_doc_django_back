from django.db import models
from django.contrib.postgres.fields import ArrayField


class Document(models.Model):
    number = models.CharField(max_length=200, null=True)
    date = models.CharField(max_length=200, null=True)
    ispolnitelFirmName = models.CharField(max_length=200, null=True)
    ispolnitelDirName = models.CharField(max_length=200, null=True)
    clientFirmName = models.CharField(max_length=200, null=True)
    clientDirName = models.CharField(max_length=200, null=True)
    cargoType = models.CharField(max_length=200, null=True)
    allAdressFrom = ArrayField(models.CharField(max_length=200), null=True)
    allAdressTo = ArrayField(models.CharField(max_length=200), null=True)
    ispOkvedNumber = models.CharField(max_length=6, null=True)
    ispOkvedText = models.CharField(max_length=200, null=True)
    clientOkvedNumber = models.CharField(max_length=6, null=True)
    clientOkvedText = models.CharField(max_length=200, null=True)
    carGrz = models.CharField(max_length=9, null=True)
    carModel = models.CharField(max_length=100, null=True)
    carType = models.CharField(max_length=100, null=True)
    carCargoMin = models.CharField(max_length=20, null=True)
    carCargoMax = models.CharField(max_length=20, null=True)
    carCargo = models.CharField(max_length=20, null=True)
    carCargo80 = models.CharField(max_length=20, null=True)
    carCargoMonth = models.CharField(max_length=20, null=True)
    carCargoYear = models.CharField(max_length=20, null=True)
    date_from = models.CharField(max_length=200, null=True)
    date_to = models.CharField(max_length=200, null=True)
    ispolnitelUrAdress = models.CharField(max_length=200, null=True)
    ispolnitelInn = models.CharField(max_length=12, null=True)
    ispolnitelKpp = models.CharField(max_length=200, null=True)
    ispolnitelOgrn = models.CharField(max_length=13, null=True)
    ispolnitelBik = models.CharField(max_length=9, null=True)
    ispolnitelRs = models.CharField(max_length=20, null=True)
    ispolnitelBank = models.CharField(max_length=200, null=True)
    ispolnitelDirShort = models.CharField(max_length=200, null=True)
    clientUrAdress = models.CharField(max_length=200, null=True)
    clientInn = models.CharField(max_length=12, null=True)
    clientKpp = models.CharField(max_length=9, null=True)
    clientOgrn = models.CharField(max_length=13, null=True)
    clientBik = models.CharField(max_length=9, null=True)
    clientRs = models.CharField(max_length=20, null=True)
    clientBank = models.CharField(max_length=200, null=True)
    clientDirShort = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.id

class DocFile(models.Model):
    file = models.FileField(upload_to='media')
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
