# Generated by Django 3.0.2 on 2020-06-27 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_vk', '0032_auto_20200624_1835'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='Post',
        ),
    ]
