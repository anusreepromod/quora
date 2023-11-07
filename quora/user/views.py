import json
from django.http import  JsonResponse
from django.shortcuts import  render
from django.db.models import Q
from . models import *

# Create your views here.

def fnlogin(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            logi_obj = login.objects.get(username=username, password=password)
            request.session['log'] = logi_obj.id
            posts_obj = Posts.objects.all()  
            
            return render(request, 'dashboard.html',{'posts': posts_obj})
    except Exception as e:
        print(e)

    return render(request, 'login.html')

def signup(request):
    try:
        email = request.POST['email']
        u_obj = login.objects.filter(username=email).exists()
        print(u_obj)
        if u_obj == False:
            name = request.POST['name']
            password = request.POST['password']
            user_obj = User(name=name, email=email) 
            user_obj.save()
            login_obj = login(username=email, password=password,
                              user_id_id=user_obj.id)
            login_obj.save()
            return render(request, 'login.html', {'message': 'User registered successfully'})
        else:
            return render(request, 'register.html', {'message': 'User already exist'})
    except Exception as e:
        print(e)
    return render(request, 'register.html')

def fnposts(request):
    try:
        if request.method == 'POST':
            user_id = request.session['log']
            title = request.POST['title']
            posts = request.POST['posts']
            post_obj = Posts(post_title=title,posts=posts,user_id_id=user_id)
            post_obj.save()
            return render(request, 'dashboard.html')
    except Exception as e:
        print(e)
    return render(request, 'dashboard.html')

def postcomment(request):
    try:
        if request.method == 'POST':
            userid = request.POST['user_id']
            id = request.POST['id']
            comments = request.POST['comment']
            comment_obj = Comments(post_id_id=id,comments=comments,user_id_id=userid)
            comment_obj.save()
            return JsonResponse({'message':'Posted Successfully'})
    except Exception as e:
        print(e)
    return render(request, 'dashboard.html')


def getposts(request):
    posts = Posts.objects.all()  
    post_obj = [{'id': i.id, 'title': i.post_title, 'posts': i.posts}  for i in posts]
    return JsonResponse({'posts': post_obj})
    
def postlike(request):
    try:
        if request.method == 'POST':
            userid = request.POST['user_id']
            id = request.POST['id']
            u_obj = Likes.objects.filter(Q(post_id_id=id) or Q(user_id_id=userid)).exists()
            print(u_obj)
            if u_obj== False:
                count=1
                like_obj = Likes(post_id_id=id,likes=count,user_id_id=userid)
                like_obj.save()
                print(like_obj)
                return render(request, 'dashboard.html')
            else:
                return render(request, 'dashboard.html')
    except Exception as e:
        print(e)
    return render(request, 'dashboard.html')


def viewcomment(request):
    try:
        post_id= request.POST['id']
        com= Comments.objects.filter(post_id_id=post_id)
        com_obj = [{'comments': i.comments}  for i in com]
        return JsonResponse({'comments':com_obj})
    except Exception as e:
        print(e)

def fnlogout(request):
    del request.session['log']
    return render(request, 'login.html')