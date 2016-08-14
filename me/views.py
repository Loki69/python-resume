from django.shortcuts import render,render_to_response
from django.http.response import HttpResponse
from django.template.loader import get_template
from .models import Persona, Skill, Project,Article

# def last_news(count=1):
#     return Project.objects.all()

def index(request):

    return render_to_response('home_page/home.html',{'page_menu':1, 'projects':get_projects[:3]})

def projects(request):
    return render_to_response('projects/projects.html',{'page_menu':2,'projects':get_projects})

def project(request,project_id=1):
    return render_to_response('projects/project.html',{'page_menu':2,
            'project': get_project(project_id)})

def contact(reques):
    return render_to_response('contact/contact.html',{'page_menu':4})

def about_me(request):
    persona = None
    article = None
    try:
        persona = Persona.objects.get(id=1)
        article = Article.objects.order_by('id').filter(owner=persona.id)[0]

    except Persona.DoesNotExist:
        persona = Persona.objects.create("Pavel Garani")
    return render_to_response('about_me/about_me.html',{
        'persona':persona,
        'page_menu':3,
        'about_me':article})

def get_projects():
    persona = Persona.objects.get(id=1)
    return Project.objects.order_by('id').filter(owner=persona.id)

def get_project(id):
    return Project.objects.get(id=id)