from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('', views.index, name="index"),
    path('register', views.register, name='register'),
    path('all', views.all_user, name='all_user'),
    path('profil/<str:login>', views.profil, name='profil'),
    path('subscribe/<int:user_id>', views.subscribe, name='subscribe'),
    path('my_subscribe/<str:user_login>', views.my_subscribe, name='my_subscribe'),
    path('my_subscribers/<str:login>', views.my_subscribers, name='my_subscribers'),
    path('all_like/<int:post_id>', views.all_like, name='all_like'),
    path('like/<int:post_id>', views.like, name='like'),
    path('all_comment/<int:post_id>', views.all_comment, name='all_comment'),
    path('comment_add/<int:post_id>', views.comment_add, name='comment_add'),
    path('message/<int:user_id>', views.message, name='message'),
    path('messages/<int:user_id>', views.messages, name='messages'),
    path('search/', views.search, name='search'),
    path('addPhoto/<int:user_id>', views.addPost, name='addPhoto'),
    path('avatar/>', views.avatar, name='avatar'),
]
