from django_celery_beat.models import PeriodicTask, IntervalSchedule


schedule, created = IntervalSchedule.objects.get_or_create(
    every=24,
    period=IntervalSchedule.HOURS,
)


def set_schedule():
    PeriodicTask.objects.create(
        interval=schedule,
        name='Check last login and block inactive users',
        task='education.tasks.check_last_login_and_block_inactive_users',
    )
