from django.conf.urls import url
from .views import index ,aboutMe, projects, project

urlpatterns = [
    url(r'^$', index ),
    url(r'^about/', aboutMe ),
    url(r'^project/all', projects),
    url(r'^project/get/(?P<project_id>\d+)/$', project),
]
