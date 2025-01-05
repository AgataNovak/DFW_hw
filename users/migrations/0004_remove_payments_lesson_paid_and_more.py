# Generated by Django 5.1.4 on 2025-01-05 15:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0005_delete_payment'),
        ('users', '0003_remove_user_city_remove_user_phone_user_country_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payments',
            name='lesson_paid',
        ),
        migrations.AlterField(
            model_name='payments',
            name='course_paid',
            field=models.ForeignKey(blank=True, help_text='Введите статус оплаты', null=True, on_delete=django.db.models.deletion.CASCADE, to='education.course', verbose_name='Курс оплачен'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payment_amount',
            field=models.PositiveIntegerField(help_text='Введите сумму к оплате', verbose_name='Cумма к оплате'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payment_date',
            field=models.DateTimeField(auto_now_add=True, help_text='Введите дату оплаты', verbose_name='Дата оплаты'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payment_method',
            field=models.CharField(choices=[('наличные', 'Наличные'), ('перевод на счет', 'Перевод на счет'), ('онлайн оплата', 'Онлайн оплата')], help_text='Введите способ оплаты', max_length=50, verbose_name='Способ оплаты'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]