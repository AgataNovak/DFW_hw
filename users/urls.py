from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import UserCreateApiView, PaymentCreateAPIView
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path("register/", UserCreateApiView.as_view(), name="register"),
    path("token/", TokenObtainPairView.as_view(), name="login"),
    path("payment/", PaymentCreateAPIView.as_view(), name="payment"),
]
