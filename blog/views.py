from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import contact, Blog, BlogComment, userprofile, Liked
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import json
# from blog.templatetags import extras
# Create your views here.

def home(request):
    # messages.error(request,'Hello world')
    post = Blog.objects.all()
    liked = [i for i in post if Liked.objects.filter(post=i,user=request.user)]
    print(liked)
    return render(request,'index.html',{'post':post,'liked':liked})

def contact1(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('description')
        cant = contact(name=name,email=email,description=desc)
        cant.save()
        messages.success(request,'Your Message have been sent')
    return render(request,'contact.html')

def blogpost(request,id):
    post = Blog.objects.filter(post_id=id)[0]
    comments = BlogComment.objects.filter(post=post,parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)

    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    return render(request,'blogpost.html',{'post':post,'comments':comments,'replyDict':replyDict})

def about(request):
    return render(request,'about.html')

def signin(request):
    if request.method=='POST':
        usern = request.POST['loginusername']
        passw = request.POST['passwd']
        user = authenticate(username=usern,password=passw)
        print(usern,passw)
        if user is not None:
            login(request,user)
            print("success")
            messages.success(request,'Successfully Logged In')
            return redirect('home')
            
        else:
            messages.error(request,'Invalid Creditions') 
            print("fail")
            return redirect('home')
    # return render(request,'signin.html')

def signup(request):
    if request.method=='POST':
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1 != pass2:
            messages.error(request,'Password must be same')
        myuser = User.objects.create_user(username=username,email=email,password=pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,'Your account have been Created')
        return redirect('/')

    # return render(request,'signup.html')
def signout(request):
    logout(request)
    messages.success(request,'Successfully Logged out')
    return redirect('home')

def profile(request,username):
    user = User.objects.filter(username=username)
    if user:
        prof = userprofile.objects.get(user=user[0])
        moredetail = User.objects.get(username=prof)
        post = Blog.objects.filter(user=user[0])
        return render(request,'profile.html',{'prof':prof,'user':moredetail,'post':post})
    else:
        return HttpResponse("No Such User")

def blogcomment(request):
    if request.method=='POST':
        comment = request.POST.get('Comment')
        user = request.user
        postSno= request.POST.get('PostSno')
        post = Blog.objects.get(post_id=postSno)

        parentSno = request.POST.get("parentSno")
        if parentSno == "":
            comment = BlogComment(commentt=comment,user=user,post=post)
            comment.save()
            messages.success(request,"Your Comment Have been send")
        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(commentt=comment,user=user,post=post,parent=parent)
            comment.save()
            messages.success(request,"Your Comment Reply Have been send")

    return redirect(f"/blogpost/{post.post_id}")

def follow(request):
    pass

def findusers(request):
    moredetail = User.objects.all()
    users = User.objects.all()
    print(users)
    return render(request,'findusers.html',{'user':users,'moredetail':moredetail})

def likepost(request):
    id = request.GET.get("likeid","")
    post = Blog.objects.get(post_id=id)
    user = request.user
    like = Liked.objects.filter(post=post,user=user)
    print(like)
    liked=False
    if like:
        Liked.Disliked(post=post,dislinking_user=user)
    else:
        liked=True
        Liked.Liked(post=post,liking_user=user)

    resp = {
        'liked':liked
    }
    respose = json.dumps(resp)
    return HttpResponse(respose,content_type = "application/json")
