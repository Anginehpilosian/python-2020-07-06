from django.shortcuts import redirect, render

from .models import Shirt, User

# Create your views here.


def index(request):
    return render(request, 'index.html')


def sign_up(request):
    print(request.POST)
    # add a user to the DB
    user_who_just_signed_up = User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        social_security_number=request.POST['social_security_number'],
        password=request.POST['password']
    )

    print('user_who_just_signed_up.id: ', user_who_just_signed_up.id)

    if 'uid' not in request.session:
        # add a user id to session
        request.session['uid'] = user_who_just_signed_up.id

    return redirect('/users')


def users(request):
    # get all the users

    context = {
        "users": User.objects.all()
    }
    return render(request, 'users.html', context)


def shirts(request):
    context = {
        "shirtzzz": Shirt.objects.all()
    }
    return render(request, 'shirts.html', context)


def shirts_new(request):
    return render(request, 'shirts_new.html')


def shirts_create(request):
    print(request.POST)
    user_who_is_logged_in = User.objects.get(id=request.session['uid'])
    # add a shirt to the db
    uploaded_shirt = Shirt.objects.create(
        color=request.POST['color'],
        size=request.POST['size'],
        material=request.POST['material'],
        upload_by=user_who_is_logged_in
    )
    print('uploaded_shirt: ', uploaded_shirt)
    return redirect('/shirts')
