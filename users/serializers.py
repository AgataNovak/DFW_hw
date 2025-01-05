from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User, Payment
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class UserDetailSerializer(serializers.ModelSerializer):
    payment_history = PaymentsSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "email", "phone_number", "avatar", "city", "payment_history"]


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Добавление пользовательских полей в токен
        token['username'] = user.username
        token['email'] = user.email

        return token
