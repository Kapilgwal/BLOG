from .views import AuthorViewSet, ArticleViewSet, CommentViewSet, RegisterView, LoginView
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='article')
router.register(r'authors', AuthorViewSet, basename='authors')
router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]

urlpatterns += router.urls
