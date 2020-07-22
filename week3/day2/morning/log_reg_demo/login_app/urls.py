from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index),
    path('account', views.view_account),


    path('register', views.register_user),
    path('logout', views.logout_session),
    path('login', views.login_user),

]
