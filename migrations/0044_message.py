# Generated by Django 3.0.2 on 2020-07-01 11:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_vk', '0043_auto_20200629_2130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_vk.User')),
                ('message_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='my_vk.Post')),
            ],
        ),
    ]
