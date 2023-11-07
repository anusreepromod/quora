from django.db import models

# Create your models here.
# I have created all the models in this page only. Generally few of them should be created in admin side

class User(models.Model):
    name=models.CharField(max_length=100)
    email = models.CharField(max_length=100)

class login(models.Model):
    username = models.EmailField()
    password = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Posts(models.Model):
    post_title=models.CharField(max_length=20)
    posts=models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
class Comments(models.Model):
    comments=models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)

class Likes(models.Model):  
    likes=models.IntegerField()
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)