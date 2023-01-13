from .models import Document, DocFile
from rest_framework import serializers


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id',
                  'number',
                  'date',
                  'date_from',
                  'date_to',
                  'ispolnitelFirmName',
                  'ispolnitelDirName',
                  'clientFirmName',
                  'clientDirName',
                  'cargoType',
                  'allAdressFrom',
                  'allAdressTo',
                  'ispOkvedNumber',
                  'ispOkvedText',
                  'clientOkvedNumber',
                  'clientOkvedText',
                  'carGrz',
                  'carModel',
                  'carType',
                  'carCargoMin',
                  'carCargoMax',
                  'carCargo',
                  'carCargo80',
                  'carCargoMonth',
                  'carCargoYear',
                  'ispolnitelUrAdress',
                  'ispolnitelInn',
                  'ispolnitelKpp',
                  'ispolnitelOgrn',
                  'ispolnitelBik',
                  'ispolnitelRs',
                  'ispolnitelBank',
                  'ispolnitelDirShort',
                  'clientUrAdress',
                  'clientInn',
                  'clientKpp',
                  'clientOgrn',
                  'clientBik',
                  'clientRs',
                  'clientBank',
                  'clientDirShort')


class DocFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocFile
        fields = ('id', 'title', 'file')