from rest_framework import serializers
from .models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ['id', 'username', 'bio', 'profile_picture', 'password']
    extra_kwargs = {
      'password' : {'write_only':True}
    }

  def create(self, validated_data):
    user = CustomUser.objects.create_user(
      username=validated_data['username'],
      password=validated_data['password'],
      bio=validated_data.get('bio', ''),
      profile_picture=validated_data.get('profile_picture', None)
        )
    return user

class LoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField(write_only = True) #write_only means the field can be used when sending data in, but will NOT be included when sending data out

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ['id', 'username', 'bio', 'profile_picture', 'followers']
    

    

  


