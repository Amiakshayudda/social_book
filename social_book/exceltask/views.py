from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd
from .models import Book
from django.db.models import Count
from django.utils import timezone
from . serializers import BookSerializer, NewBookSerializer
# from django.http import HttpResponse
from django.core.files.storage import default_storage
# from rest_framework.decorators import api_view
import io
from . models import NewBook
import sqlalchemy
from sqlalchemy import create_engine, text
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ReadExcelView(APIView):
    def post(self, request):
        file = request.FILES.get('file')

        if not file:
            return Response({'error': 'No file provided'})

        try:
            excfile = pd.read_excel(file)
        except pd.errors.ParserError:
            return Response({'error': 'Invalid file format'})

        for _, row in excfile.iterrows():
            title = row['Title']
            author = row['Author']
            price = row['Price']
            date_of_sale = row['Date of sale']

            book = Book(title=title, author=author, price=price, date_of_sale=date_of_sale)
            book.save()

        return Response({'message': 'Books inserted successfully'})


class GetTopBook(APIView):
    def post(self, request):
        author = request.POST['author']

        if not author:
            return Response({'error': 'Please provide author'})
        else:
            books = Book.objects.filter(author=author).annotate(sale_count=Count('title')).order_by('-sale_count')
            most_sold_book = books.first()
            sold_copies = Book.objects.filter(title=most_sold_book.title, author=most_sold_book.author).count()
            total_earnings = sold_copies * most_sold_book.price

            # For calculating increase/decrease in sale compared to last month
            current_month_last_day = timezone.now()
            current_month_start_day = current_month_last_day.replace(day=1)
            last_month_last_day = current_month_start_day - timezone.timedelta(days=1)
            last_month_start_day = last_month_last_day.replace(day=1)

            last_month_sold_copies = Book.objects.filter(title=most_sold_book.title, author=most_sold_book.author, date_of_sale__range=(last_month_start_day, last_month_last_day)).count()
            current_month_sold_copies = Book.objects.filter(title=most_sold_book.title, author=most_sold_book.author, date_of_sale__range=(current_month_start_day, current_month_last_day)).count()

            last_month_revenue = last_month_sold_copies * most_sold_book.price
            current_month_revenue = current_month_sold_copies * most_sold_book.price

            if last_month_revenue != 0:
                growth_or_shrink = (current_month_revenue / last_month_revenue) * 100
            else:
                growth_or_shrink = "Dont have last month's data to compare"

            # serializer = BookSerializer(most_sold_book)

            data = {
                'book_name': most_sold_book.title,
                'Total copies sold': sold_copies,
                'Total earnings': total_earnings,
                'Last month earnings': last_month_revenue,
                'Current month earnings': current_month_revenue,
                "Growth or shrink": growth_or_shrink
            }
            # return Response(serializer.data)
            return Response(data)


# Creating an excel file and populating it with the data from db (not working currently)
# @api_view(['GET'])
# def CreateExcelDFView(request):

#     all_entries = Book.objects.all().values()

#     df = pd.DataFrame.from_records(all_entries)

#     # writer = pd.ExcelWriter('TestData.xlsx', engine='xlsxwriter')

#     output = io.BytesIO()
#     writer = pd.ExcelWriter(output, engine='xlsxwriter')

#     df.to_excel(writer, sheet_name='Sheet1', index=False)

#     writer.save()
#     output.seek(0)

#     df = pd.read_excel(output, engine='openpyxl')

#     response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
#     response['Content-Disposition'] = 'attachment; filename="TestData.xlsx"'
#     df.to_excel(response, index=False)

#     return response


class ReadNewExcelView(APIView):
    def post(self, request):
        file = request.FILES.get('file')

        if not file:
            return Response({'error': 'No file found. Please select a file'})

        try:
            exclfile = pd.read_excel(file)
        except pd.errors.ParserError:
            return Response({'error': 'Invalid file format. Please upload excel file'})

        for _, row in exclfile.iterrows():
            nid = row['Id']
            try:
                existing_newbook = NewBook.objects.get(id=nid)
                existing_newbook.title = row['Title']
                existing_newbook.author = row['Author']
                existing_newbook.price = row['Price']
                existing_newbook.date_of_sale = row['Date of sale']
                existing_newbook.save()
            except NewBook.DoesNotExist:
                book = NewBook(id=nid, title=row['Title'], author=row['Author'], price=row['Price'], date_of_sale=row['Date of sale'])
                book.save()

        return Response({'message': 'Books saved successfully'})

class SimpleReadExcelView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        author = request.POST['author']
        title = request.POST['title']
        price = request.POST['price']

        engine = sqlalchemy.create_engine('postgresql://postgres:Akshay%4095520@localhost:5432/social_book')

        query = text("select * from exceltask_book where author = :value1")

        params = {'value1': author}

        df = pd.read_sql_query(query, engine, params=params)
        print(df)

        data = df.to_json(orient='records')
        # print(data)
        return Response(data)
        # return JsonResponse(data, safe=False)