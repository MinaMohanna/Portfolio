from django.shortcuts import render
from .models import Project

# Create your views here.

def projects(request):
    projects_list = Project.objects.all()

    return render(request, 'projects/projects.html', {
        'projects' : projects_list
    })