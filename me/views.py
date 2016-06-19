from django.shortcuts import render,render_to_response
from django.http.response import HttpResponse
from django.template.loader import get_template
from .models import Persona, Skill

def index(request):
    return render_to_response('index.html')

def aboutMe(request):
    result = None
    try:
        result = Persona.objects.get(id=1)
    except Persona.DoesNotExist:
        result = Persona.objects.create("Pavel Garani")
    return render_to_response('about_me.html',{'persona':result})