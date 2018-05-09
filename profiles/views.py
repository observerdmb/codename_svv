from django.shortcuts import render

def my_page(request):
    template = 'profile.html'
    context = {}
    return render(request, template, context)

def empty_view(request):
    template = 'empty.html'
    context = {}
    return render(request=request, template_name=template, context=context)

# Create your views here.
