from django.db import models

class Post(models.Model):
  author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name = 'posts')
  title = models.CharField(max_length=150)
  content = models.TextField()
  attachment = models.ImageField(upload_to='attachment_pics/' ,blank=True)
  created_at =  models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.title} by {self.author.username}"
  
class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
  author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name = 'user_comments')
  content= models.TextField()
  created_at =  models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"Comment by {self.author.username}"


  


    
