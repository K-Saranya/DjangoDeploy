from django.urls import path
from .views import *
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('signup', signup_page, name='signup'),
    path('login', login_page, name='login'),
    path('signup_function/', signup_function),
    path('test',test_view),

]
