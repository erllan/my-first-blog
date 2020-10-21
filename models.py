from django.db import models
from datetime import datetime


class User(models.Model):
    login = models.CharField(max_length=500, unique=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    password = models.CharField(max_length=500)
    avatar = models.ImageField("фото профиля", default='/avatar/anonim-avatar.jpg', upload_to='avatar/', )
    follofing = models.ManyToManyField('self', blank=True, symmetrical=False)

    def __str__(self):
        return self.login


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_user')
    post = models.ImageField("добавьте пост", upload_to='posts/', blank=True)
    comment = models.TextField(blank=True)
    like = models.ManyToManyField(User, null=True, blank=True)
    date = models.DateTimeField(default=datetime.now)


class Comment(models.Model):
    comment_to = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now)


class Dialog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Message(models.Model):
    message_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='messages')
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, )
    message = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now)
    # dialog = models.ForeignKey(Dialog, on_delete=models.CASCADE, related_name='DIALOG')
