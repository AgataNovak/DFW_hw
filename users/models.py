from django.contrib.auth.models import AbstractUser
from django.db import models

from education.models import Lesson, Course


class User(AbstractUser):
    username = models.CharField(max_length=50, verbose_name="username", blank=True, null=True)
    email = models.EmailField(unique=True, verbose_name="Email", help_text="Введите Ваш e-mail")
    avatar = models.ImageField(upload_to="media/users/avatars/", verbose_name='Аватар', blank=True, null=True, help_text="Загрузите Ваше фото")
    phone_number = models.CharField(max_length=35, verbose_name="Телефон", blank=True, null=True,
                                    help_text="Введите номер телефона")
    country = models.CharField(max_length=100, verbose_name="Страна", blank=True, null=True,
                               help_text="Введите Вашу страну")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username",]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Payments(models.Model):
    PAYMENT_CHOICES = [
        ("наличные", "наличные"),
        ("перевод на счет", "перевод на счет"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,

        blank=True,
        null=True,
        verbose_name="Пользователь",
    )
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата оплаты")
    course_paid = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Курс оплачен",
    )
    lesson_paid = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Урок оплачен",
    )
    payment_amount = models.DecimalField(
        max_digits=9, decimal_places=2, verbose_name="Сумма оплаты"
    )
    payment_method = models.CharField(
        max_length=50, choices=PAYMENT_CHOICES, verbose_name="Способ оплаты"
    )

    def __str__(self):
        return f"{self.user} - {self.payment_amount} - {self.payment_date}"

    class Meta:
        verbose_name = "Платёж"
        verbose_name_plural = "Платежи"
        ordering = ["payment_date"]
