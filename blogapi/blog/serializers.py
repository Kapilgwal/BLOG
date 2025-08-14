from rest_framework import serializers
from .models import Author, Article, Comments

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        source='author',
        write_only=True
    )

    class Meta:
        model = Article
        fields = [
            'id',
            'author',
            'author_id',   
            'title',
            'tags',
            'content',
            'written_on',
            'updated_on'
        ]

    def get_author(self, obj):
        return f"{obj.author.first_name} {obj.author.last_name}"

class CommentSerializer(serializers.ModelSerializer):
    article = serializers.CharField(source='article.title', read_only=True)
    article_id = serializers.PrimaryKeyRelatedField(
        queryset=Article.objects.all(),
        source='article',
        write_only=True,
        required = False
    )

    class Meta:
        model = Comments
        fields = [
            'id',
            'article', 
            'article_id',   
            'comment',
            'written_on'
        ]
