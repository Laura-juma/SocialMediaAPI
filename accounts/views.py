from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate
from .models import CustomUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, LoginSerializer, MyProfileSerializer, ProfileSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from notifications.models import Notification


class RegisterView(APIView):
  permission_classes=[AllowAny]
  def post(self, request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
      user = serializer.save()

      token, created = Token.objects.get_or_create(user=user)

      return Response({
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "bio": user.bio,
                },
                "token": token.key
            }, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class LoginView(APIView):
  def post(self, request):
    serializer = LoginSerializer(data = request.data)
    if serializer.is_valid():
      username = serializer.validated_data['username']
      password = serializer.validated_data['password']

      user = authenticate(username=username, password=password)

      if user is not None:
        token, created = Token.objects.get_or_create(user=user)

        return Response({
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "bio": user.bio,
                },
                "token": token.key
            })
      
      return Response({"error": "Invalid username or password"},
                      status=status.HTTP_401_UNAUTHORIZED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MyProfileView(APIView):
  permission_classes = [IsAuthenticated]
  def get(self, request):
    serializer = MyProfileSerializer(request.user)
    return Response(serializer.data)
  
  def patch(self, request):
    serializer = MyProfileSerializer(request.user, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileView(APIView):
  permission_classes = [IsAuthenticated]
  def get(self, request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)

class FollowUserView(APIView):
  permission_classes =[IsAuthenticated]
  def post(self,request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)

    if request.user == user:
      return Response(
    {"error": "You cannot follow yourself"},
    status=status.HTTP_400_BAD_REQUEST)

    if user in request.user.following.all():
      return Response({"error":"You already follow user"}, status =status.HTTP_400_BAD_REQUEST)
    
    request.user.following.add(user)

    Notification.objects.create(
      recipient =user,
      actor = request.user,
      verb = 'followed',
      target = user
    )

    return Response({"message": "User followed successfully"})

class UnfollowUserView(APIView):
  permission_classes = [IsAuthenticated]
  def post(self,request,user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    request.user.following.remove(user)
    return Response({"message":"User unfollowed successfully!"})

class LogoutView(APIView):
  permission_classes = [IsAuthenticated]
  def post(self, request):
    request.user.auth_token.delete()
    return Response({"message": "You have logged out!"})
     

 


      


    
       
        

    
    
      

  

  




