# Generated by Django 3.0.2 on 2020-06-19 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_vk', '0009_auto_20200619_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='follovers',
        ),
    ]
