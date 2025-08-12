from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Author, Article, Comments
from .serializers import AuthorSerializer, ArticleSerializer, CommentSerializer


class AuthorAPIView(APIView):
    def get(self, request, id=None):
        if id:
            author = get_object_or_404(Author, id=id)
            serializer = AuthorSerializer(author)
            return Response(serializer.data)
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Author created successfully'}, status=status.HTTP_201_CREATED)
        return Response({'msg': 'Invalid data', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        id = request.data.get("id")
        if not id:
            return Response({'msg': 'Please provide an ID to update'}, status=status.HTTP_400_BAD_REQUEST)

        author = get_object_or_404(Author, id=id)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Author updated successfully'}, status=status.HTTP_200_OK)
        return Response({'msg': 'Invalid data', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        id = request.data.get("id")
        if not id:
            return Response({'msg': 'Please provide an ID to delete'}, status=status.HTTP_400_BAD_REQUEST)

        author = get_object_or_404(Author, id=id)
        author.delete()
        return Response({'msg': 'Author deleted successfully'}, status=status.HTTP_200_OK)


class ArticleAPIView(APIView):
    def get(self, request, id=None):
        if id:
            article = get_object_or_404(Article, id=id)
            serializer = ArticleSerializer(article)
            return Response(serializer.data)
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Article created successfully'}, status=status.HTTP_201_CREATED)
        return Response({'msg': 'Invalid data', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None):
        if not id:
            return Response({'msg': 'Please provide an ID to update'}, status=status.HTTP_400_BAD_REQUEST)

        article = get_object_or_404(Article, id=id)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Article updated successfully'}, status=status.HTTP_200_OK)
        return Response({'msg': 'Invalid data', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        if not id:
            return Response({'msg': 'Please provide an ID to delete'}, status=status.HTTP_400_BAD_REQUEST)

        article = get_object_or_404(Article, id=id)
        article.delete()
        return Response({'msg': 'Article deleted successfully'}, status=status.HTTP_200_OK)


class CommentAPIView(APIView):
    def get(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        comments = Comments.objects.filter(article=article)
        if not comments.exists():
            return Response({'msg': 'No comments found'}, status=status.HTTP_200_OK)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        
        data = request.data.copy()
        data['article_id'] = article.id

        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
