from django.shortcuts import render,render_to_response
from django.http.response import HttpResponse
from django.template.loader import get_template
from .models import Persona, Skill, Project

# def last_news(count=1):
#     return Project.objects.all()

def index(request):
    return render_to_response('about_me/about_me.html',{'persona':Persona.objects.get(id=1)})

# def projects(request):
#     return render_to_response('me/last_news.html',{'news':last_news()})

# def project(request,project_id):
#     try: 
#         project = Project.objects.get(id=project_id)
#     except ObjectDoesNotExist:
#         raise Http404
#     return render_to_response('me/last_news.html',{'project':project})

# def aboutMe(request):
#     result = None
#     try:
#         result = Persona.objects.get(id=1)
#     except Persona.DoesNotExist:
#         result = Persona.objects.create("Pavel Garani")
#     return render_to_response('me/about_me.html',{'persona':result})
