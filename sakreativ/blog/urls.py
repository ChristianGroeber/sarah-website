from django.conf.urls import url
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^tinymce/', include('tinymce.urls')),
]