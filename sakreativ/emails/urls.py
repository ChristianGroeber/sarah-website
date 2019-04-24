from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('newsletter/<newsletter_id>/', views.send_newsletter),
]