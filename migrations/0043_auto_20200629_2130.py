# Generated by Django 3.0.2 on 2020-06-29 15:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_vk', '0042_auto_20200629_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
