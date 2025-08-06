from django.http import JsonResponse
from .models import Author, Article
from .serializers import AuthorSerializer, ArticleSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

@csrf_exempt
def author(request, id=None):
    if request.method == 'GET':
        if id is not None:
            try:
                auth = Author.objects.get(id=id)
                serializer = AuthorSerializer(auth)
                return JsonResponse(serializer.data, safe=False)
            except Author.DoesNotExist:
                return JsonResponse({'error': 'Author not found'}, status=404)
        else:
            authors = Author.objects.all()
            serializer = AuthorSerializer(authors, many=True)
            return JsonResponse(serializer.data, safe=False)
        
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AuthorSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg': 'Author created successfully'}, status=201)
        
        return JsonResponse({'msg': 'Invalid data', 'errors': serializer.errors}, status=400)


@csrf_exempt
def article(request, id=None):
    if request.method == 'GET':
        if id is not None:
            try:
                art = Article.objects.get(id=id)
                serializer = ArticleSerializer(art)
                return JsonResponse(serializer.data, safe=False)
            except Article.DoesNotExist:
                return JsonResponse({'error': 'Article not found'}, status=404)
        else:
            articles = Article.objects.all()
            serializer = ArticleSerializer(articles, many=True)
            return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg': 'Article created successfully'}, status=201)
        
        return JsonResponse({'msg': 'Invalid data', 'errors': serializer.errors}, status=400)
