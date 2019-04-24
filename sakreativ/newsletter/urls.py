from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='newsletter'),
    path('unsubscribe/<unsubscribe_id>/', views.unsubscribe),
    path('subscribe/', views.subscribe),
    path('subscribe/<subscriber_mail>/', views.subscribe_from_url),
    path('delete/<newsletter_id>/', views.delete_newsletter)
]
