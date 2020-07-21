from django.contrib import messages
from django.shortcuts import redirect, render

import bcrypt

from .models import User


# Create your views here.
def index(request):
    return render(request, 'index.html')


def register_user(request):
    print(request.POST)
    # validate the post data
    errors = User.objects.register_validator(request.POST)
    # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        # has the password
        print(request.POST['password'])
        hash_browns = bcrypt.hashpw(
            request.POST['password'].encode(), bcrypt.gensalt()).decode()
        print('hash_browns: ', hash_browns)
        # create a user
        freshly_created_user = User.objects.create(
            username=request.POST['username'],
            email=request.POST['email'],
            password=hash_browns,
        )
        # add the user to session
        request.session['uid'] = freshly_created_user.id
        print('*'*50)
        print(freshly_created_user.password)
        return redirect('/account')


def view_account(request):
    return render(request, 'account.html')


def logout_session(request):
    request.session.clear()
    return redirect('/')


def login_user(request):
    print(request.POST)
    # check the db for an email match
    user_with_matching_email = User.objects.filter(
        email=request.POST['email']).first()
    print('user_with_matching_email: ', user_with_matching_email)

    if user_with_matching_email != None:
        # check the db for a matching password
        is_pw_matched = bcrypt.checkpw(
            request.POST['password'].encode(), user_with_matching_email.password.encode())
        if is_pw_matched:
            # we have a matched password
            # session
            request.session['uid'] = user_with_matching_email.id
            return redirect('/account')
    else:
        return redirect('/')
