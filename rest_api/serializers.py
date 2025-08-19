from rest_framework import serializers
from .models import *
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(self,user):
        token = super(MyTokenObtainPairSerializer,self).get_token(user)
        token["username"] = user.username
        token["email"] = user.email
        return token, user.username, user.email
 
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = ['user_id', "user_name", "email", "age"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
