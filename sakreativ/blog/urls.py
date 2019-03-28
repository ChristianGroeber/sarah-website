from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/<id>/', views.blog_post),
    path('ueber-mich', views.ueber_mich, name='ueber_mich'),
    path('galerie', views.gallery, name='galerie'),
    path('galerie/<gallery>', views.gallery),
]