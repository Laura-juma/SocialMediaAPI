from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate
from .models import CustomUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


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

class ProfileView(APIView):
  permission_classes = [IsAuthenticated]
  def get(self, request):
    serializer = ProfileSerializer(request.user)
    return Response(serializer.data)
  
  def patch(self, request):
    serializer = ProfileSerializer(request.user, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 
class FollowUserView(APIView):
  permission_classes =[IsAuthenticated]
  def post(self,request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.user == user:return Response(
    {"error": "You cannot follow yourself"},
    status=status.HTTP_400_BAD_REQUEST)
    if user in request.user.following.all():
      return Response({"error":"You already follow user"}, status =status.HTTP_400_BAD_REQUEST)
    request.user.following.add(user)
    return Response({"message": "User followed successfully"})

class UnfollowUserView(APIView):
  permission_classes = [IsAuthenticated]
  def post(self,request,user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    request.user.following.remove(user)
    return Response({"message":"User unfollowed successfully!"})


     

 


      


    
       
        

    
    
      

  

  




