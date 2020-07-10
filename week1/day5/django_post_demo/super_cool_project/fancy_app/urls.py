from django.urls import path

from . import views

urlpatterns = [
    # GET routes
    path('', views.index),
    path('dashboard/<str:id>', views.dashboard),
    # POST routes
    path('sign_up', views.sign_up),
]
