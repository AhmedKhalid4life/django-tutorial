from rest_framework import serializers
from .models import Author, Books, Review


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Author
        fields= "__all__"

    
    
class BookSerializer(serializers.ModelSerializer):
    author= AuthorSerializer()
    class Meta:
        model= Books
        fields= "__all__"
    
    #create
    def create(self, validated_data):
        author_data = validated_data.pop('author')
        author,_ = Author.objects.get_or_create(**author_data)
        book = Books.objects.create(author= author, **validated_data)
        return book
    


class ReviewSerializers(serializers.ModelSerializer):
    book= BookSerializer()
    
    class Meta:
        model= Review
        fields= "__all__"

    
    def create(self, validated_data):
        books_data = validated_data.pop('book')
        book,_ = Books.objects.get_or_create(**books_data)
        book = Review.objects.create(book = book, **validated_data)
        return book