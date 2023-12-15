from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from .views import register , getuser , reservation , tasks , create_staff_user , rooms , oneRoom

urlpatterns = [
    path('register/', register , name='auth_register'),
    path('getuser/', getuser , name='auth_getuser'),
    path('reservation/' , reservation , name='reservation'),
    path('tasks/' , tasks , name='tasks'),
    path('create_staff_user/' , create_staff_user , name='create_staff_user'),
    path('rooms/' , rooms , name='rooms'),
    path('oneRoom/<int:room_id>' , oneRoom , name='oneRoom'),
]
    