from django.shortcuts import HttpResponse, render

# Create your views here.


def home(request):

    # Do some stuff
    # get data form the DB
    # run some business logic

    # return HttpResponse('It works!')
    # return HttpResponse('<h1>Hello World!</h1>')
    return render(request, 'index.html')


def products(request):
    return render(request, 'products.html')
