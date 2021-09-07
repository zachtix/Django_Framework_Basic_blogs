from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def hello(request):
    #Query Data From Model
    data = Post.objects.all()
    return render(request,'index.html', {'posts':data})

def page1(request):
    return render(request, 'page1.html')

def createForm(request):
    return render(request,'form.html')

def addBlog(request):
    name = request.POST['name']
    description = request.POST['description']
    return render(request, 'result.html', {'name':name, 'description':description})

def addUser(request):
    username = request.POST['username']
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    password = request.POST['password']
    cpassword = request.POST['cpassword']
    if password == cpassword:
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Already Username')
            return redirect('/registerForm')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Already E-mail')
            return redirect('/registerForm')
        else:
            user = User.objects.create_user(
                username = username,
                password = password,
                email = email,
                first_name = fname,
                last_name = lname
                )
            user.save()
            return redirect('/')
    else:
        messages.info(request, 'Password not Match')
        return redirect('/registerForm')

def registerForm(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')