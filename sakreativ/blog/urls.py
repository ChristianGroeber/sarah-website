from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/<id>/', views.blog_post),
    path('shop/', views.shop, name='shop'),
    path('shop/<product>/add/', views.add),
    path('shop/checkout/<product>/<operation>/', views.add),
    path('shop/checkout/', views.checkout),
    path('shop/<category>/', views.shop),
    path('shop/checkout/address/', views.address),
    path('ueber-mich', views.ueber_mich, name='ueber_mich'),
    path('galerie', views.gallery, name='galerie'),
    path('galerie/<gallery>', views.gallery),
]
