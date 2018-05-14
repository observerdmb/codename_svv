# coding: utf8
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def my_page(request):
    template = 'profile.html'
    context = {}
    if request.user.is_authenticated:
        current_user = User.objects.get(username=request.user)
        context['username'] = current_user.username
        context['email'] = current_user.email
        context['first_name'] = current_user.first_name
        context['last_name'] = current_user.last_name
        # context['nick_name'] = user.person.nick_name
        # context['country'] = user.person.country
        # context['city'] = user.person.city
        # context['about_me'] = user.person.about_me
    else:
        pass
    return render(request, template, context)

def login_user(request):
    template = 'login.html'
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        auth_user = authenticate(request, username=username, password=password)
        if auth_user is not None:
            login(request, auth_user)
            return redirect(my_page)
        else:
            pass
    else:
        pass
    return render(request, template, context)

def empty_view(request):
    template = 'empty.html'
    context = {}
    return render(request=request, template_name=template, context=context)

# Create your views here.
