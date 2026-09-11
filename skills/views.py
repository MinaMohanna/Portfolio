from django.shortcuts import render

# Create your views here.

def skills(request):
    skills_list = [
        'HTML',
        'CSS',
        'JavaScript',
        'Python',
        'Django,'
        'Git',
        'GitHub'
    ]
    return render(request, 'skills/skills.html' , {
        'skills': skills_list
    })
