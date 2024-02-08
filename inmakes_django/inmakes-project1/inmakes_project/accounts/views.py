from django.shortcuts import render,redirect
from django .contrib.auth.models import User
from django.contrib import messages,auth
# Create your views here.

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        c_pass=request.POST['c_pass']
        if password==c_pass:
            if User.objects.filter(email=email).exists():
                messages.info(request,'email alresy taken')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'username alredy taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
                return redirect('login')
                
        else:
            messages.info(request,'password is not match')
    return render(request,'registration.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'plese register')
            return redirect('register')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
            

