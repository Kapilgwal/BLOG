from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets
from django.shortcuts import get_object_or_404
from .models import Author, Article, Comments
from .serializers import AuthorSerializer, ArticleSerializer, CommentSerializer
from .pagination import AuthorPagination, AritclePagination
from rest_framework import generics,filters

class AuthorViewSet(viewsets.ModelViewSet):
        queryset = Author.objects.all()
        serializer_class = AuthorSerializer
        pagination_class = AuthorPagination
        filter_backends = [filters.SearchFilter]
        search_fields = ['first_name','last_name','gender']

class ArticleViewSet(viewsets.ModelViewSet):
        queryset = Article.objects.all().order_by('-updated_on')
        serializer_class = ArticleSerializer
        pagination_class = AritclePagination
        filter_backends = [filters.SearchFilter]
        search_fields = ['tags','title']

class CommentViewSet(viewsets.ModelViewSet):
        queryset = Comments.objects.all()
        serializer_class = CommentSerializer