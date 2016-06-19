from django.conf.urls import url
from .views import index ,aboutMe

urlpatterns = [
    url(r'^$', index ),
    url(r'^about/', aboutMe )
]
