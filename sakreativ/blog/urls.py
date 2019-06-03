from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/<id>/', views.blog_post),
    path('shop/', views.shop, name='shop'),
    path('shop/checkout/', views.checkout),
    path('shop/checkout/address/', views.address),
    path('shop/checkout/<product>/<operation>/', views.add),
    path('shop/<product>/<size>/<operation>/', views.add),
    path('shop/<product>/<operation>/', views.add),
    path('shop/<category>/', views.shop),
    path('ueber-mich', views.ueber_mich, name='ueber_mich'),
    path('galerie', views.gallery, name='galerie'),
    path('galerie/<gallery>', views.gallery),
]
