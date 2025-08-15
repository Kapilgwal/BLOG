from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets
from django.shortcuts import get_object_or_404
from .models import Author, Article, Comments
from .serializers import AuthorSerializer, ArticleSerializer, CommentSerializer,RegistrationSerializer
from .pagination import AuthorPagination, AritclePagination
from rest_framework import generics,filters
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

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

class RegisterView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'user': serializer.data,
                'token': token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response(
                {'error': 'Email and password are required.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(request, username=email, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials.'},status=status.HTTP_401_UNAUTHORIZED)
