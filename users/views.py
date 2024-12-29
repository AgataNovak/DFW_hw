from rest_framework_simplejwt.views import TokenObtainPairView

from users.serializers import MyTokenObtainPairSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from users.models import User, Payments
from users.serializers import UserSerializer, PaymentsSerializer, UserDetailSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return self.queryset.filter(id=self.request.user.id)

    def perform_update(self, serializer):
        serializer.save()


class PaymentsViewSet(viewsets.ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_set_fields = ("payment_method", "paid_course", "paid_lesson")
    ordering_fields = ("payment_date",)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
