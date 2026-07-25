from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Notification(models.Model):
  recipient = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='received_notifications')
  actor = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='sent_notifications')
  verb = models.CharField(max_length = 150)
  target_content_type = models.ForeignKey(ContentType, on_delete = models.CASCADE, null=True, blank=True)
  target_object_id = models.PositiveIntegerField(null=True, blank=True)
  target = GenericForeignKey('target_content_type', 'target_object_id')
  timestamp = models.DateTimeField(auto_now_add=True)
  is_read = models.BooleanField(default=False)

  class Meta:
    ordering = ['-timestamp']

  def __str__(self):
    return f'{self.actor} {self.verb} {self.target or "something" }'


