from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('sign_up', views.sign_up),
    path('my_profile', views.show_user_profile),
    path('log_out', views.log_out),
    path('shirts/create', views.create_a_shirt),
    path('clubs/create', views.create_a_club),
    path('clubs/<int:club_id>/join', views.join_a_club),
]
