from django.shortcuts import redirect, render

from .models import User

# Create your views here.


def index(request):
    return render(request, 'index.html')


def sign_up(request):
    print(request.POST)
    # add a user to the DB
    User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        social_security_number=request.POST['social_security_number'],
        password=request.POST['password']
    )

    return redirect('/users')


def users(request):
    # get all the users

    context = {
      "users": User.objects.all()
    }
    return render(request, 'users.html', context)
