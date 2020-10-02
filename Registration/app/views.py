from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'app/index.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists !!')
                return redirect('registration')
            
            elif User.objects.filter(email = email).exists():
                messages.info(request,'email already exists !!')
                
                
            else:
                user = User.objects.create_user(username=username, password=password1,email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request,"Created succefully !!")
        
        else:
            messages.info(request,'password not match')
            return redirect('registration')
        
    

    return render(request, 'app/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username = username,password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,"invalid credintial")
        return redirect('login')
    return render(request, 'app/login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')
