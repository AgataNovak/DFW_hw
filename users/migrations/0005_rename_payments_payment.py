# Generated by Django 5.1.4 on 2025-01-06 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0005_delete_payment'),
        ('users', '0004_remove_payments_lesson_paid_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Payments',
            new_name='Payment',
        ),
    ]