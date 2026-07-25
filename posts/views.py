from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from .permissions import IsAuthorOrReadOnly
from .models import Post, Comment, Likes
from .serializers import PostSerializer, CommentSerializer
from accounts.models import CustomUser
from notifications.models import Notification

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
    comment = serializer.save(author=self.request.user)
    if comment.post.author != self.request.user:
      Notification.objects.create(
        recipient = comment.post.author,
        actor = self.request.user,
        verb = "commented on",
        target = comment.post
    )

class FeedView(APIView):
  permission_classes = [IsAuthenticated]
  def get(self, request):
   user_following = request.user.following.all()
   queryset = Post.objects.filter(author__in=user_following)
   serializer = PostSerializer(queryset, many=True)

   return Response(serializer.data)

class LikeView(APIView):
  permission_classes = [IsAuthenticated]
  def post(self, request,pk):
    post =  get_object_or_404(Post, pk=pk)
    
    like, created =Likes.objects.get_or_create(
      post = post,
      user = request.user
    )

    if not created:
      return Response ({
        "message" : "You already liked this post"
      }, status = status.HTTP_400_BAD_REQUEST)
    
    if post.author != request.user:
      Notification.objects.create(
        recipient = post.author,
        actor = request.user,
        verb = 'liked',
        target = post
      )
    
    return Response ({
        "message" : "The post has been liked successfully"
      }, status = status.HTTP_201_CREATED)
    
class UnLikeView(APIView):
  permission_classes = [IsAuthenticated]
  def delete(self,request, pk):
    post = get_object_or_404(Post, pk=pk)
    like = Likes.objects.get(user=request.user, post=post)
    like.delete()

    return Response({'Post has been unliked'},
                    status=status.HTTP_204_NO_CONTENT)



    



