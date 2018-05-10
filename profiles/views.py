from django.shortcuts import render
from django.contrib.auth.models import User


def my_page(request):
    template = 'profile.html'
    context = {}
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        context['username'] = user.username
        context['first_name'] = user.person.first_name
        context['last_name'] = user.person.last_name
        context['nick_name'] = user.person.nick_name
        context['country'] = user.person.country
        context['city'] = user.person.city
        context['about_me'] = user.person.about_me
    else:
        pass
    return render(request, template, context)


def registration(request):
    if request.method == 'POST':
        user_data = request.POST
        new_user = User.objects.create_user(
            username=user_data['username'],
            email=user_data['email'],
            password=user_data['password'],
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            )
        new_user.save()
    template = 'registration.html'
    context = {}
    return render(request, template, context)


def empty_view(request):
    template = 'empty.html'
    context = {}
    return render(request=request, template_name=template, context=context)

# Create your views here.
