from rest_framework import serializers
from .models import Author, Article

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.name', read_only=True)
    
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        source='author',
        write_only=True,
        required=False 
        )

    class Meta:
        model = Article
        fields = [
            'id',
            'author',
            'author_id',    
            'title',
            'content',
            'written_on',
            'updated_on'
        ]
