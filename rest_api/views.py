from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from .models import *


# Create your views here.

class MyTokenObtainView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = MyTokenObtainPairSerializer

class CrudOperations(APIView):
    permission_classes = (AllowAny)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  
            refresh = RefreshToken.for_user(user)  
            access = str(refresh.access_token)
            return Response(
                {
                    "user": serializer.data,
                    "refresh": str(refresh),
                    "access": access,
                },
                status=status.HTTP_201_CREATED,)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    def get(self, request, user_id = None):
        try:
            if user_id == None:
                user = UserDetail.objects.all()
                serializer = UserDetailSerializer(user, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                user = UserDetail.objects.get(user_id= user_id)
                serializer = UserDetailSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, user_id):
        try:
            if user_id:
                user = UserDetail.objects.get(user_id= user_id)
                serializer = UserDetailSerializer(user,data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, user_id):
        try:
            if user_id:
                user = UserDetail.objects.get(user_id=user_id)
                user.delete()
                return Response("User deleted successfully", status=status.HTTP_204_NO_CONTENT)    
            else:
                return Response("User not found", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
        
    

def product_page(request):
    product_data = MobileTable.objects.all()
    # print(product_data)
    return render(request, "product.html", {"product": product_data})