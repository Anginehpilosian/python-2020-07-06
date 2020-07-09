from django.urls import path

from . import views

urlpatterns = [
    # path('', include('intro_app.urls'))
    path('', views.home),
    path('products', views.products),
]
