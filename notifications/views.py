from django.shortcuts import render
from .models import Notification
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from .serializers import NotificationSerializer

class NotificationView(ListAPIView):
  queryset = Notification.objects.all()
  serializer_class = NotificationSerializer
  permission_classes = [IsAuthenticated]

  def get_queryset(self):
    print("Current user:",self.request.user)
    return self.request.user.received_notifications.all()



