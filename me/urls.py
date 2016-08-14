from django.conf.urls import url
from .views import index,projects,about_me,contact

urlpatterns = [
    url(r'^$', index ),
    url(r'projects/$', projects ),
    # url(r'project/$', project ),
    url(r'about/$', about_me),
    url(r'contact/$', contact ),
]
