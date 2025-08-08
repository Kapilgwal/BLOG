from django.urls import path
from . import views

urlpatterns = [
    path('author/', views.author, name='author_list_create'),          
    path('author/<int:id>/', views.author, name='author_detail'),     
    path('article/', views.article, name='article_list_create'),
    path('article/<int:id>/', views.article, name='article_detail'),
]
