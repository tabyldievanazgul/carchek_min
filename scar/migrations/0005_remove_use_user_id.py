# Generated by Django 3.1 on 2020-11-14 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scar', '0004_car_use_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='use',
            name='user_id',
        ),
    ]
