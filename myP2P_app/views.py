# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponseRedirect, render_to_response
from forms import PostFormRegistration, PostFormBorrowers, PostFormLenders
from .models import Lenders, Borrowers


# Create your views here.

def register_details(request):

    context = {"borrower_form": PostFormBorrowers(),
               "lender_form": PostFormLenders()
               }

    return render(request, 'registration/register_details.html', context)

def register_details_lenders(request):
    if request.method == "POST":
        form = PostFormLenders(request.POST)
        if form.is_valid():
            form.save()
            return redirect('investing')
        else:
            return render(request, 'register_user', {"error": "invalid details"})
    lender_form = PostFormLenders()
    return render(request, 'registration/lender_details.html', {'lender_form':lender_form})

def register_details_borrowers(request):

    borrower_form = PostFormBorrowers()
    return render(request, 'registration/borrower_details.html', {'borrower_form':borrower_form})

def index(request):
    return render(request, 'myP2P_app/index.html', {})

@login_required(login_url='login')
def borrowing(request):
    if request.method == "POST":
        form = PostFormBorrowers(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.borrower_user_id = request.user
            profile.save()
        else:
            return render(request, 'register_user', {"error": "invalid details"})

    try:
        result = Borrowers.objects.get(borrower_user_id=request.user.id)
        # all_result = Borrowers.objects.all()

        print result.borrower_outstanding_balance
        return render(request, 'registration/borrowing.html', {'result': result})
    except Exception as e:
        print e.args
        return redirect('register_user')


@login_required(login_url='login')
def investing(request):
    if request.method == "POST":
        form = PostFormLenders(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.lender_user_id = request.user
            profile.save()
        else:
            return render(request, 'register_user', {"error": "invalid details"})

    try:
        result = Lenders.objects.get(lender_user_id=request.user.id)
        print result
        return render(request, 'registration/investing.html', {'result': result})
    except Exception as e:
        print e.args
        return redirect('register_user')
        # return HttpResponse("ERROR - no user account available. Please register again.")

    # active_user = request.user.id
    # result = Lenders.objects.get(lender_user_id=active_user)
    #
    # return render(request,'registration/investing.html', {'result':result})

def faq(request):
    return render (request, 'registration/faq.html', {})

def register_user(request):
    if request.method == "POST":
        form = PostFormRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('register_details')
        # else:
        #     return redirect('register_user')
    else:
        form = PostFormRegistration()
    return render(request, "registration/register.html", {'form': form})

