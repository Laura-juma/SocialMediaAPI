from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
  bio = models.TextField()
  profile_picture = models.ImageField(upload_to='profiles_pics/' ,blank=True)
  following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)#symmetrical is false mean if A follows B it does not auomatically mean B follows A

  def __str__(self):
    return self.username





