from django.shortcuts import redirect, render


# Render functions
def index(request):
    # return HttpResponse('<h1>Firday!</h1>')
    return render(request, 'index.html')


def dashboard(request, id):
    print('***********')
    print(id)
    contextz = {
        "name": id
    }

    return render(request, 'dashboard.html', contextz)

# Redirect functions


def sign_up(request):
    print(request.POST["first_name"])
    # go to the database and save the user info

    return redirect(f'/dashboard/{request.POST["first_name"]}')
