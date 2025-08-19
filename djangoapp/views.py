from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import *

# Create your views here.

def signup_page(request):
    return render(request, 'signup.html')

def login_page(request):
    return render(request, 'login.html')



def signup_function(request):
    if request.method == 'POST':
        firstname = request.POST.get("first_name")
        lastname = request.POST.get("last_name")
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        print(firstname,lastname,username,email,password)
        if password == confirm_password:
            print(password)
            if User.objects.filter(username = username).exists():
                return redirect('signup')
                # print('lllllllllllllllllllllllllllllllllllllllllllllllllll')
            elif User.objects.filter(email = email).exists():
                return redirect('signup')
                # print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
            else:
                user = User.objects.create_user(first_name = firstname, last_name = lastname, username = username, email = email, password = user.set_password(password)
                )
                refresh = str(MyTokenObtainPairSerializer.get_token(user))
                access = str(refresh.access_token)
                print(refresh)
                print(access)
                user.save()
                return Response({'refresh': refresh, 'access': access}, status=200)
        
        else:
            return redirect('signup')
            # print('jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj')
            
            
def test_view(request):
    print("Inside view function")
    return HttpResponse("Hiii")