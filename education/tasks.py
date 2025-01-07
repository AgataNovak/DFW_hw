from datetime import datetime, timedelta
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from celery import shared_task

from users.models import User


def email_update_notification_to_subscriber(email, course):
    send_mail('Обновление курса!', f'Курс {course} обновлён.', EMAIL_HOST_USER, [email])


@shared_task
def check_last_login_and_block_inactive_users():
    min_last_day_activity = datetime.now() - timedelta(days=30)
    users = User.objects.all()
    for user in users:
        if user.last_login < min_last_day_activity:
            user.is_active = False
            user.save()
        else:
            user.is_active = True
            user.save()

