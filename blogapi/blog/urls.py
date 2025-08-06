from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# router = DefaultRouter()
# router.register(r'author', views.AuthorViewSet, basename='author')
# router.register(r'article', views.ArticleViewSet, basename='article')

urlpatterns = [
    # path('', include(router.urls)),
    path('author/', views.author, name = 'author'),
    path('author/<int:id>/', views.author, name = 'author'),
    path('article/', views.article, name = 'article'),
    path('article/<int:id>', views.article, name = 'article'),
]
