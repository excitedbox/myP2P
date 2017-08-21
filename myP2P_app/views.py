# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from forms import PostFormRegistration

# Create your views here.

#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         if user.is_active:
#             login(request, user)
#             return redirect("/") # Redirect to a success page.
#         else:
#             pass  #Return a 'disabled account'  error message
#     else:
#         pass #Return an 'invalid login' error message.

def register(request):
    if request.method == 'POST':
        form = PostFormRegistration(request.POST)
        if form.is_valid():
            new_user = form.save()
            type = request.POST.get('dropdown')
            if (type == 'borrower'):
                redirect(reverse("registration/borrowing.html"))
            else:
                redirect(reverse("registration/investing.html"))
            # new_user = authenticate(username=form.cleaned_data['username'],
            #                         password=form.cleaned_data['password']),
            # login(request, new_user)
        return redirect(reverse("index"))
    else:
        form = PostFormRegistration()
        return render(request, "registration/register.html", {'form': form})

def index(request):
    return render(request, 'myP2P_app/index.html', {})

@login_required(login_url='myP2P_app/index.html')
def borrowing(request):
    return render (request, 'registration/borrowing.html', {})

@login_required(login_url='myP2P_app/index.html')
def investing(request):
    return render (request, 'registration/investing.html', {})

def faq(request):
    return render (request, 'registration/faq.html', {})




