from .views import AuthorViewSet,ArticleViewSet,CommentViewSet
from rest_framework.routers  import DefaultRouter

router = DefaultRouter()
router.register(r'articles',ArticleViewSet,basename='article')
router.register(r'authors',AuthorViewSet,basename='authors')
router.register(r'comments',CommentViewSet,basename='comments')

urlpatterns = router.urls