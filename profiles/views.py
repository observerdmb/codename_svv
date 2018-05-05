from django.shortcuts import render

def empty_view(request):
    template = 'profile.html'
    context = {}
    return render(request=request, template_name=template, context=context)

# Create your views here.
