# Generated by Django 3.0.2 on 2020-06-29 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_vk', '0035_auto_20200629_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='follofing',
            field=models.ManyToManyField(blank=True, related_name='_user_follofing_+', to='my_vk.User'),
        ),
    ]
