from django.urls import path
from .views import *
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('create/', CrudOperations.as_view()),
    path('get/<int:user_id>/', CrudOperations.as_view()),
    path('get/', CrudOperations.as_view()),
    path('edit/<int:user_id>/', CrudOperations.as_view()),
    path("delete/<int:user_id>/", CrudOperations.as_view()),
    path('user/token/obtain/', MyTokenObtainView.as_view()),
    path('user/token/refresh/', jwt_views.TokenRefreshView.as_view() ),
    
]
