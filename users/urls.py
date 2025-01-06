from django.urls import path

from .views import MyTokenObtainPairView, UserCreateApiView, PaymentCreateAPIView
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('register/', UserCreateApiView.as_view(), name='register'),
    path('token/', MyTokenObtainPairView.as_view(), name='login'),
    path('payment/', PaymentCreateAPIView.as_view(), name='payment'),
]

