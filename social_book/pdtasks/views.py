from django.shortcuts import render
from rest_framework.views import APIView
import pandas as pd
from exceltask.models import NewBook
from exceltask.serializers import NewBookSerializer
from rest_framework.response import Response
import sqlalchemy
from sqlalchemy import create_engine, text

# Create your views here.

class PdExcelTask(APIView):
    def post(self, request):
        author = request.POST['author']

        # books = NewBook.objects.filter(author=author)
        # serialized_data = NewBookSerializer(books, many=True)
        # print(serialized_data.data)
        # return Response(serialized_data.data)

        engine = sqlalchemy.create_engine('postgresql://postgres:Akshay%4095520@localhost:5432/social_book')

        query = text("select * from exceltask_newbook")

        df = pd.read_sql_query(query, engine)

        return Response({'mesg': ''})
