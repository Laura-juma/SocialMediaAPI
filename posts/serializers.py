from .models import Post, Comment
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = ['title', 'content', 'created_at', 'updated_at']

  def validate_content(self, value):
    if len(value.strip()) < 5:
      raise serializers.ValidationError("Post cannot be less than 5 characters")
    return value

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = ['post', 'content', 'created_at', 'updated_at']

  def validate_content(self, value):
    if not value.strip(): #python treats an empty string as False
      raise serializers.ValidationError("Comment cannot be empty")
    return value







