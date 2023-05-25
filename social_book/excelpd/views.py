from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee, ExcelFile
import pandas as pd
from excelpd.serializers import EmployeeSerializer
from rest_framework.views import APIView
from django.conf import settings
from exceltask.models import NewBook

# Create your views here.

def export_data_to_excel(request):
    objs = Employee.objects.all()

    data = []

    for obj in objs:
        data.append({
            'id': obj.id,
            'name': obj.name,
            'address': obj.address,
            'phone': obj.phone
        })
    pd.DataFrame(data).to_excel('TestOutput.xlsx')

    return JsonResponse({'message': 'Excel file created'})
    # books = NewBook.objects.all()
    # data = []
    # for book in books:
    #     data.append({
    #         'id': book.id,
    #         'title': book.title,
    #         'author': book.author,
    #         'price': book.price,
    #         'date_of_sale': book.date_of_sale
    #     })
    # pd.DataFrame(data).to_excel('TestOutput.xlsx')

    # return JsonResponse({'message': 'Excel file created'})


class WriteExcelToDb(APIView):
    def post(self, request):
        file = request.FILES.get('file')

        if not file:
            return JsonResponse({'error': 'No file provided'})

        obj = ExcelFile.objects.create(file=file)
        path = str(obj.file)
        path = f'{settings.BASE_DIR}\{settings.MEDIA_URL}\{path}'

        df = pd.read_excel(path)
        print(df)

        return JsonResponse({'message': 'File uploaded at {path}'})
