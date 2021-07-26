from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class contact(models.Model):
    msg_id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name

class customer(models.Model):
    cust_id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    number = models.IntegerField()
    password = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Blog(models.Model):
    post_id= models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,default='')
    content = models.CharField(max_length=1000,default='')
    publish_date = models.DateTimeField(default=now)
    thumbnail = models.ImageField(upload_to='images', default='')
    
    def __str__(self):
        return self.title

class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    commentt = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Blog,on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.commentt[0:13] + "..." + "by " + self.user.username
    
class userprofile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    dob = models.DateField()
    gender = models.CharField(max_length=100,default='')
    relationship = models.CharField(max_length=100,default='')
    mobile = models.IntegerField(default=0)
    hometown = models.CharField(max_length=100,null=True)
    profile_pic = models.ImageField(upload_to='profile_pic',blank=True)  
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)  

    def __str__(self):
        return self.user.username

class Following(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followed = models.ManyToManyField(User, related_name="followed")

    @classmethod
    def follow(cls, user, anather_account):
        obj, create =cls.objects.get_or_create(user=user)
        obj.followed.add(anather_account)
        print("followed")

    @classmethod
    def unfollow(cls, user, anather_account):
        obj, create =cls.objects.get_or_create(user=user)
        obj.followed.remove(anather_account)
        print("unfollow")


class Liked(models.Model):
    user = models.ManyToManyField(User,related_name="Liking_user")
    post = models.OneToOneField(Blog,on_delete=models.CASCADE)

    @classmethod
    def Liked(cls, post, liking_user):
        obj, create =cls.objects.get_or_create(post=post)
        obj.user.add(liking_user)

    @classmethod
    def Disliked(cls, post, dislinking_user):
        obj, create =cls.objects.get_or_create(post=post)
        obj.user.remove(dislinking_user)
