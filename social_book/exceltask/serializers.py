from rest_framework import serializers
from . models import Book, NewBook

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class NewBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewBook
        fields = ('id', 'title', 'author', 'price', 'date_of_sale')