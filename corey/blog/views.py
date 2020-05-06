from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from .forms import blogwriter
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.

post=Post.objects.all()
user=User.objects.all()
def home (request):
    
    context={
        'posts':post
    }

    return render(request,"blog/index.html",context)
    

def about(request):
    return HttpResponse("<h1>HOME PAGE OF BLOG</h1>") 

def abtuser(request):
    context={
        'users':user
    }
    return render(request,"blog/abtuser.html",context)

def blogwrite(request):
    if request.method=="GET":
        form=blogwriter()
        return render(request,"blog/blogwrite.html",{"form":form})
    
    if request.method=='POST':
        print ("POST CALLED")
        form=blogwriter(request.POST)
        
        if form.is_valid():
            form.save(commit=True)  
            return redirect("BLOGHOME")
        else:
            messages.error(request,"Error occured")
            return render(request,"blog/blogwrite.html",{"form":form})
    