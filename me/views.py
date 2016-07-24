from django.shortcuts import render,render_to_response
from django.http.response import HttpResponse
from django.template.loader import get_template
from .models import Persona, Skill, Project

# def last_news(count=1):
#     return Project.objects.all()

def index(request):
    return render_to_response('home_page/home.html',{'menu':1})

def projects(request):
    return render_to_response('projects/projects.html',{'menu':2})

def aboutMe(request):
    persona = None
    article = None
    try:
        persona = Persona.objects.get(id=1)
        article = Article.objects.filter(owner=persona.id).orde_by('id').get(1)

    except Persona.DoesNotExist:
        persona = Persona.objects.create("Pavel Garani")
    return render_to_response('about_me/about_me.html',{'persona':persona,'menu':3,'about_me':article})