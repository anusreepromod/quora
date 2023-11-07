from django.urls.conf import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('login/', views.fnlogin),
    path('signup/', views.signup, name='signup'),
    path('posts/', views.fnposts, name='posts'),
    path('getposts/', views.getposts),
    path('comment/', views.postcomment),
    path('viewcomment/', views.viewcomment),
    path('like/', views.postlike,name='likebutton'),
    path('logout/', views.fnlogout, name='logout'),
]