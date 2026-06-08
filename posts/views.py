from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from .permissions import IsAuthorOrReadOnly
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  permission_classes = [IsAuthenticated,
                        IsAuthorOrReadOnly]
  filter_backends = [SearchFilter]
  search_fields = ['title', 'content']

  def perform_create(self, serializer):
    serializer.save(author=self.request.user)

   
class CommentViewSet(viewsets.ModelViewSet):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  permission_classes = [IsAuthenticated,
                        IsAuthorOrReadOnly]

  def perform_create(self, serializer):
    serializer.save(author=self.request.user)


