from django.shortcuts import HttpResponse, render, HttpResponseRedirect, redirect
from .models import User, Post, Message
from django.urls import reverse
import json
from django.core.files.storage import FileSystemStorage


def search(request):
    if request.method == 'POST':
        a = request.POST['search']
        users = User.objects.filter(login__startswith=a) or User.objects.filter(name__startswith=a)
        if users:
            return render(request, 'my_vk/search.html', {'users': users})
        else:
            return HttpResponse('никого не найдено')


def login(request):
    error = ''
    if request.method == 'POST':
        login = request.POST['login']
        user = User.objects.get(login=login)
        if user.password == request.POST['password']:
            userData = {'login': user.login, 'id': user.id, 'name': user.name, 'avatar': user.avatar.url}
            request.session['User'] = userData
            return redirect('index')
        error = 'неверный логин или пароль'
    return render(request, 'my_vk/authorization.html', {'error': error})


def logout(request):
    del request.session['User']
    return redirect('login')


def index(request):
    try:
        user = request.session['User']
    except:
        user = None
    if user == None:
        return redirect('login')

    user1 = User.objects.get(id=user['id'])
    post = list(Post.objects.filter(user__in=user1.follofing.all()).order_by('-date'))
    print(like)
    return render(request, 'my_vk/index.html', {'user': user1, 'posts': post})


def register(request):
    if request.method == 'POST':
        post = request.POST
        user = User(name=post['name'],
                    surname=post['surname'],
                    login=post['login'],
                    password=post['password'])
        user.save()
        if user:
            userData = {'login': user.login, 'id': user.id, 'name': user.name, 'avatar': user.avatar.url}
            request.session['User'] = userData
            return redirect('index')
    return render(request, 'my_vk/register.html')


def subscribe(request, user_id):
    user = User.objects.get(id=user_id)
    a = request.session['User']
    sesionUser = User.objects.get(id=a['id'])
    if sesionUser.follofing.filter(id=user_id):
        sesionUser.follofing.remove(user)
        result = 'no'
    else:
        sesionUser.follofing.add(user)
        result = 'yes'
    return HttpResponse(json.dumps({"result": result}), content_type="application/json")


def all_user(request):
    users = User.objects.all()
    user = request.session['User']
    return render(request, 'my_vk/all_user.html', {'users': users, 'user': user})


def profil(request, login):
    is_follof = 0
    profil = User.objects.get(login=login)
    user = request.session['User']
    sesionUser = User.objects.get(id=user['id'])
    post = profil.post_user.all().order_by('-date')
    if sesionUser.follofing.filter(login=login):
        is_follof += 1
    return render(request, 'my_vk/profil.html', {'profil': profil, "user": user, 'post': post, 'is_follof': is_follof})


def my_subscribers(request, login):
    user = request.session['User']
    test = User.objects.get(login=login)
    follof = test.user_set.all()
    return render(request, 'my_vk/my_subscribers.html', {'test': follof, "user": user})


def my_subscribe(request, user_login):
    user = request.session['User']
    user1 = User.objects.get(login=user_login)
    s = user1.follofing.all()
    return render(request, 'my_vk/my_subscribe.html', {'test': s, "user": user})


def all_like(request, post_id):
    post = Post.objects.get(id=post_id)
    like = post.like.all()
    return HttpResponse(like)


def like(request, post_id):
    sessid = request.session['User']
    user = User.objects.get(id=sessid['id'])
    post = Post.objects.get(id=post_id)
    test = post.like.filter(id=sessid['id'])
    if test:
        post.like.remove(user)
        result = 'unlike'
    else:
        post.like.add(user)
        result = 'like'
    return HttpResponse(json.dumps({"result": result}), content_type="application/json")


def all_comment(request, post_id):
    post = Post.objects.get(id=post_id)
    allCommet = post.comments.order_by('-date')
    return render(request, 'my_vk/comments.html', {"comments": allCommet, 'post': post})


def comment_add(request, post_id):
    sessUser = request.session['User']
    user = User.objects.get(id=sessUser['id'])
    post = Post.objects.get(id=post_id)
    addComment = post.comments.create(from_user=user, comment_to=post, comment=request.POST['comment'])
    addComment.save()
    comment = addComment.comment
    user = user.login
    return HttpResponse(json.dumps({"comment": comment, 'user': user}), content_type="application/json")


def message(request, user_id):
    sessUser = request.session['User']
    for_user = User.objects.get(id=user_id)
    from_user = User.objects.get(id=sessUser['id'])
    if request.method == 'POST':
        b = request.POST['message']
        a = Message(message_to=for_user,
                    from_user=from_user,
                    message=b)
        a.save()
        return HttpResponse(json.dumps({"message": b, 'user': from_user.login}), content_type="application/json")


def messages(request, user_id):
    sessUser = request.session['User']
    from_user = User.objects.get(id=sessUser['id'])
    for_user = User.objects.get(id=user_id)
    for_user_message = Message.objects.filter(message_to=from_user, from_user=for_user)
    from_user_message = Message.objects.filter(from_user=from_user, message_to=for_user)
    all_messages = for_user_message.union(from_user_message).order_by('date')
    return render(request, 'my_vk/message.html',
                  {'all_messages': all_messages, 'from_user': from_user,
                   'for_user': for_user})


def addPost(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage(location='media/posts')
        filename = fs.save(myfile.name, myfile)
        add = Post(post='/posts/' + filename, user=user)
        add.save()
        return HttpResponseRedirect(reverse('profil', args=(user.login,)))


def avatar(request):
    if request.method == 'POST':
        sessUser = request.session['User']
        myfile = request.FILES['avatar']
        user = User.objects.get(id=sessUser['id'])
        fs = FileSystemStorage(location='media/avatar')
        filename = fs.save(myfile.name, myfile)
        user.avatar = '/avatar/' + filename
        user.save()
        return HttpResponseRedirect(reverse('profil', args=(user.login,)))
