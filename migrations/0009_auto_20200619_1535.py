# Generated by Django 3.0.2 on 2020-06-19 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_vk', '0008_auto_20200619_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='anonim-avatar.jpg', upload_to='avatar/', verbose_name='фото профиля'),
        ),
    ]
