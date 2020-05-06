from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserRegsiterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def reguser(request):
    
    if request.method=='GET':
        form=UserRegsiterForm()
        return render(request,"user/reguser.html",{'form':form})
    
    if request.method=="POST":
        form=UserRegsiterForm(request.POST)
        #print(request.POST)
        if form.is_valid():
            form.save(commit=True)            
            username=form.cleaned_data.get("username")
            messages.success(request,"Account created. Now login") 
            return redirect("login")
        else:
            print("INVALID USER")
            messages.warning(request,"ERROR CREATING USER")
            return redirect("REGISTER-USER")

@login_required
def profile(request):
    return render(request,"user/profile.html")