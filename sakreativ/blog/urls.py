from django.conf.urls import url
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/<id>/', views.blog_post),
    path('ueber-mich', views.ueber_mich),
    path('galerie', views.gallery),
    path('galerie/<gallery>', views.gallery),
]