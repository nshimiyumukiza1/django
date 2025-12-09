from django.urls import path
from.views import LoginVeiw,RegisterView,UserList,CustomLoginView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns =[
    path('register/',RegisterView.as_view()),
    path('login/',LoginVeiw.as_view()),
    path('users/',UserList.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # login to get token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # refresh token
    path('login/jwt/', CustomLoginView.as_view(), name='jwt_login'),
]   