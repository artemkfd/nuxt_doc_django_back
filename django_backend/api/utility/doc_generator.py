from docxtpl import DocxTemplate

from api.models import DocFile
from django_backend.settings import MEDIA_ROOT


def create(doc_data):
    print('-----------------')
    print(doc_data.carGrz)
    print(doc_data.date)
    print(doc_data.number)
    doc_name = f'{doc_data.carGrz}_{doc_data.number}'
    print('----------------------')
    path = MEDIA_ROOT + '\\' + f'{doc_name}.docx'
    print('path----------------- ', path)

    template = DocFile.objects.get(title="template_doc")
    doc = DocxTemplate(template.file.open())
    context = get_context(doc_data)
    doc.render(context)
    #doc.save(path)
    doc.save(path)
    return path


def get_context(doc_data):
    print('doc_data.allAdressFrom ---- ', doc_data.allAdressFrom)
    context = {
        'docNum': doc_data.number,
        'docDate': doc_data.date,
        'DateFrom': doc_data.date_from,
        'DateTo': doc_data.date_to,
        'ispolnitelFirmName': doc_data.ispolnitelFirmName,
        'ispolnitelDirName': doc_data.ispolnitelDirName,
        'ispOkvedNumber': doc_data.ispOkvedNumber,
        'ispOkvedText': doc_data.ispOkvedText,
        'ispolnitelUrAdress': doc_data.ispolnitelUrAdress,# нужно заменить
        'ispolnitelInn': doc_data.ispolnitelInn,# нужно заменить
        'ispolnitelKpp': doc_data.ispolnitelKpp,# нужно заменить
        'ispolnitelOgrn': doc_data.ispolnitelOgrn,# нужно заменить
        'ispolnitelBik': doc_data.ispolnitelBik,# нужно заменить
        'ispolnitelRs': doc_data.ispolnitelRs,# нужно заменить
        'ispolnitelBank': doc_data.ispolnitelBank,# нужно заменить
        'ispolnitelDirShort': doc_data.ispolnitelDirShort,# нужно заменить
        'clientFirmName': doc_data.clientFirmName,
        'clientDirName': doc_data.clientDirName,
        'clientOkvedNumber': doc_data.clientOkvedNumber,# нужно заменить
        'clientOkvedText': doc_data.clientOkvedText,# нужно заменить
        'clientUrAdress': doc_data.clientUrAdress,# нужно заменить
        'clientInn': doc_data.clientInn,# нужно заменить
        'clientKpp': doc_data.clientKpp,# нужно заменить
        'clientOgrn': doc_data.clientOgrn,# нужно заменить
        'clientBik': doc_data.clientBik,# нужно заменить
        'clientRs': doc_data.clientRs,# нужно заменить
        'clientBank': doc_data.clientBank,# нужно заменить
        'clientDirShort': doc_data.clientDirShort,# нужно заменить
        'cargoType': doc_data.cargoType,
        'allAdressFrom': doc_data.allAdressFrom,
        'allAdressTo': doc_data.allAdressTo,
        'carGrz': doc_data.carGrz,# нужно заменить
        'carModel': doc_data.carModel,# нужно заменить
        'carType': doc_data.carType,# нужно заменить
        'carCargo': doc_data.carCargo,# нужно заменить
        'carCargo80': doc_data.carCargo80,# нужно заменить
        'carCargoMonth': doc_data.carCargoMonth,# нужно заменить
        'carCargoYear': doc_data.carCargoYear,# нужно заменить

    }
    return context