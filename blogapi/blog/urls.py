from django.urls import path
from .views import AuthorAPIView, ArticleAPIView, CommentAPIView

urlpatterns = [
    path('authors/', AuthorAPIView.as_view()),            
    path('authors/<int:id>/', AuthorAPIView.as_view()),   

    path('articles/', ArticleAPIView.as_view()),           
    path('articles/<int:id>/', ArticleAPIView.as_view()), 

    path('comments/<int:article_id>/',CommentAPIView.as_view())
]