from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from .views import register , getuser , reservation , tasks , create_staff_user , rooms , oneRoom

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', register , name='auth_register'),
    path('getuser/', getuser , name='auth_getuser'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('reservation/' , reservation , name='reservation'),
    path('tasks/' , tasks , name='tasks'),
    path('staffuser/' , create_staff_user , name='create_staff_user'),
    path('rooms/' , rooms , name='rooms'),
    path('room/<int:room_id>' , oneRoom , name='oneRoom'),
]
    