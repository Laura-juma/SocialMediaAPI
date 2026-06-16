from rest_framework import routers
from django.urls import path
from .views import PostViewSet, CommentViewSet, FeedView, LikeView, UnLikeView

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = router.urls
urlpatterns += [
  path('feed/', FeedView.as_view(), name='feed'),
  path('posts/<int:pk>/like', LikeView.as_view(), name='like'),
  path('posts/<int:pk>/unlike', UnLikeView.as_view(), name='unlike'),
]