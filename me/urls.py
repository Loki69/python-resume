from django.conf.urls import url
from .views import index,projects,about_me,contact,project

urlpatterns = [
    url(r'^$', index ),
    url(r'projects/$', projects ),
    url(r'project/(?P<project_id>\d+)/$', project ),
    url(r'about/$', about_me),
    url(r'contact/$', contact ),
]
