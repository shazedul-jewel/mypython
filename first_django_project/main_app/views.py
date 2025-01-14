from django.shortcuts import render

from main_app.models import Profile

# Create your views here.

def index(request):
    profile = Profile.objects.last()

    return render(request, 'index.html', {'profile':profile})

def resume(request):
    return render(request, 'resume.html')

def contact(request):
    return render(request, 'contact.html')

def projects(request):
    return render(request, 'projects.html')