from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('sign_up', views.sign_up),
    path('users', views.users),
    path('shirts', views.shirts),
    path('shirts/new', views.shirts_new),
    path('shirts/create', views.shirts_create),
]
