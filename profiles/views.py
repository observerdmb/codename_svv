from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import logout


def my_page(request):
    template = 'profile.html'
    context = {}
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        context['username'] = user.username
        context['first_name'] = user.first_name
        context['last_name'] = user.last_name
        # context['nick_name'] = user.person.nick_name
        # context['country'] = user.person.country
        # context['city'] = user.person.city
        # context['about_me'] = user.person.about_me
    else:
        pass
    return render(request, template, context)

def user_logout(request):
    logout(request)

def empty_view(request):
    template = 'empty.html'
    context = {}
    return render(request=request, template_name=template, context=context)

# Create your views here.
