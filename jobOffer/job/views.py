from django.contrib.auth import login as lg, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import UserProfile


def job_offers(request):
    return render(request=request, template_name="job offers.html", context={})




def  my_applications(request):
    return render(request=request, template_name="My application.html", context={})



def apply_now(request):
    return render(request=request, template_name="Apply_Now.html", context={})



def login(request):
    if request.method == 'POST':
        eml = request.POST['email']
        pwd = request.POST['password']
        user = authenticate(email=eml, password=pwd)
        if user is not None:
            lg(request, user)
        return redirect(template_name="job_offers.html")

    return render(request=request, template_name="login.html", context={})


def register(request):
    if request.method == 'POST':
        us = request.POST['username']
        pwd = request.POST['password']
        confirm = request.POST['confirm_password']
        eml = request.POST['email']
        user = authenticate(username=us, password=pwd, confirm_password=confirm, email=eml,)

        if pwd == confirm:
            if User.objects.filter(username=us).exists():
                return render(request, template_name='register.html', context={'error': 'usermane already registered'})
            elif User.objects.filter(email=eml).exists():
                return render(request, template_name='register.html', context={'error': 'This email is already registered'})
            else:
                user = User.objects.create_user(username=us, email=eml, password=pwd)
                UserProfile.objects.create(user=user)
                return redirect(template_name="login.html")
        else:
            return render(request, template_name='register.html', context={'error': 'Password not corresponding'})
    return render(request=request, template_name="register.html", context={})





def logout(request):
    return redirect('login')
