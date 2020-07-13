from django.shortcuts import redirect, render


# Create your views here.
def index(request):
    print('Index function')
    # check if user is signed up
    if 'username' in request.session:
      return redirect('/dashboard')
    # redirect to dashboard
    return render(request, 'index.html')


def sign_up(request):
    # POST request
    print(request.POST)
    print('Sign up function')
    # save a user to session
    username_var = request.POST['usernamez']
    # create a session key
    print('username_var: ', username_var)
    request.session['username'] = username_var
    print('request.session: ', request.session)

    if 'counter' not in request.session:
        request.session['counter'] = 1
    else:
        request.session['counter'] += 1

    return redirect('/dashboard')


def dashboard(request):
    # if the user hasn't started a session
    if 'username' not in request.session:
        return redirect('/')
        # redirect them to sign up page
    else:
        context = {
            'user': request.session['username']
        }
        return render(request, 'dashboard.html', context)


def logout(request):
    # log out the user
    del request.session['username']
    # del request.session['counter']
    print('Deleted session key username!: ', request.session)
    return redirect('/')
