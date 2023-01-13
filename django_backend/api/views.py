import os
from django.conf import settings
from api.models import Document, DocFile
from api.utility import doc_generator
from api.serializers import DocumentSerializer, DocFileSerializer

from django.http import JsonResponse, HttpResponse, Http404
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, generics


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt
def create_document(request, pk):
    print('create_document pk-----', pk)
    doc_data = Document.objects.get(id=pk)
    path = doc_generator.create(doc_data)
    print('os.path.basename(path) -- ', os.path.basename(path))
    with open(path, 'rb') as fh:
        response = HttpResponse(fh.read(),
                                content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(path)
        return response


@csrf_exempt
def documentDetail(request, pk):
    print('documentDetail')
    doc = Document.objects.filter(id=pk).values()
    print(doc)
    print(doc[0])
    # doc = doc[0]
    data = {"id": 66, "number": "Д19-03-2", 'date': '«27» декабря 2022 г.', 'ispolnitelFirmName': 'ПРОСТОР М', 'ispolnitelDirName': 'Базеева Рамиля Рясимовича', 'clientFirmName': 'МАРС ГРУПП', 'clientDirName': 'Рощупкиной Виктории Игоревны', 'cargoType': 'бытовая химия', 'allAdressFrom': ['1 адрес', '2 adress', '3 adress'], 'allAdressTo': ['1 адрес', '2 adress', '3 adress'], 'ispOkvedNumber': '49.41', 'ispOkvedText': 'Деятельность автомобильного грузового транспорта', 'clientOkvedNumber': '46.75', 'clientOkvedText': 'торговля оптовая химическими продуктами', 'carGrz': 'А123АА777', 'carModel': 'MAN TGA 12345', 'carType': 'Самосвал', 'carCargoMin': '2000', 'carCargoMax': '4000', 'carCargo': '2000', 'carCargo80': '1600', 'carCargoMonth': '6400', 'carCargoYear': '76800', 'date_from': '12.12.2022', 'date_to': '11.12.2023', 'ispolnitelUrAdress': '123456, Коминтерна 26 к 2А', 'ispolnitelInn': '781234561345', 'ispolnitelKpp': '888234596', 'ispolnitelOgrn': '1234567891023', 'ispolnitelBik': '555555555', 'ispolnitelRs': '7777ispolnitelRs', 'ispolnitelBank': 'ПАО СБЕРБАНКИНГ филиал 777', 'ispolnitelDirShort': 'Базеева Р.Р.', 'clientUrAdress': '123456, Коминтерна 26 к 2А', 'clientInn': '954234561345', 'clientKpp': '444234596', 'clientOgrn': '3534567891023', 'clientBik': '555555555', 'clientRs': '7777ispolnitelRs', 'clientBank': 'ПАО ВТБ филиал 777', 'clientDirShort': 'Рощупкина В.И.'}
    return HttpResponse(data, content_type='application/json')


@csrf_exempt
def download(request, path):
    print(path)
    download_path = os.path.join(settings.MEDIA_ROOT, path)
    print(download_path)
    if os.path.exists(download_path):
        print('path exists')
        with open(download_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(download_path)
            return response
    raise Http404


# @csrf_exempt
class DocumentList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class DocumentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to be viewed or edited.
        """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [permissions.AllowAny]


    # @csrf_exempt
class DocFileViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = DocFile.objects.all()
    serializer_class = DocFileSerializer
