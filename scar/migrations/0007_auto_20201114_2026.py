# Generated by Django 3.1 on 2020-11-14 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scar', '0006_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='use',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='use',
            name='start_date',
            field=models.DateField(),
        ),
    ]
