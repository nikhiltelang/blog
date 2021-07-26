from django.contrib import admin
from django.urls import path, include
from blog import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.home,name='home'),
    path('contact/',views.contact1,name='contact'),
    path("blogpost/<int:id>",views.blogpost,name='blogpost'),
    path('about/',views.about, name='about'),
    path('signin',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('signout',views.signout,name='signout'),
    path('profile/<str:username>',views.profile,name='profile'),
    path('blogcomment/',views.blogcomment,name='blogcomment'),
    path('follow',views.follow,name='follow'),
    path('findusers',views.findusers,name='findusers'),
    path('likepost',views.likepost,name='likepost'),
]   
