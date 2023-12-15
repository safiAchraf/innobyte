from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from .views import register , getuser

urlpatterns = [
    path('register/', register , name='auth_register'),
    path('getuser/', getuser , name='auth_getuser'),
]