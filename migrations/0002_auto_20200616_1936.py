# Generated by Django 3.0.2 on 2020-06-16 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_vk', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(null=True, upload_to='avatar/', verbose_name='фото профиля'),
        ),
        migrations.DeleteModel(
            name='Session',
        ),
    ]
