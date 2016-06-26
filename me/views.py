from django.shortcuts import render,render_to_response
from django.http.response import HttpResponse
from django.template.loader import get_template
from .models import Persona, Skill, Project

def index(request):
    return render_to_response('me/last_news.html',{'news':last_news()})

def last_news(count=1):
    return Project.objects.all()


def aboutMe(request):
    result = None
    try:
        result = Persona.objects.get(id=1)
    except Persona.DoesNotExist:
        result = Persona.objects.create("Pavel Garani")
    return render_to_response('me/about_me.html',{'persona':result})
