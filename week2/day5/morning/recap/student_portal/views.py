from django.shortcuts import redirect, render

from .models import Shirt, Student


# Create your views here.
def index(request):
    print('index function!')
    return render(request, "index.html")


def sign_up(request):
    print('sign_up function!')
    print(request.POST)
    # do some stuff

    # create the user in the db
    newStudent = Student.objects.create(
        first_name=request.POST["first_name"],
        last_name=request.POST["last_name"]
    )
    # session
    request.session["user_id"] = newStudent.id
    request.session["first_name"] = newStudent.first_name
    request.session["last_name"] = newStudent.last_name

    return redirect('/my_profile')


def show_user_profile(request):
    print('profile function!')
    # if we don't have a student
    # send them back to the signup page
    if "user_id" not in request.session:
        return redirect("/")

    # get the user from the db using session user_id
    logged_in_student = Student.objects.get(id=request.session["user_id"])
    context = {
        "user_id": request.session["user_id"],
        "first_name": request.session["first_name"],
        "last_name": request.session["last_name"],
        "all_shirtzzz" : Shirt.objects.all(),
        # "my_shirtzzz" : Shirt.objects.filter(owner=logged_in_student),
        "my_shirtzzz" : logged_in_student.shirts.all(),
    }
    return render(request, 'profile.html', context)


def log_out(request):
    request.session.clear()  # ??
    # ...
    return redirect('/')
#     c = ClassName.objects.get(id=1)
# c.delete()

def create_a_shirt(request):
    print(request.POST)
    # Where is the owner from?

    logged_in_student = Student.objects.get(id=request.session["user_id"])

    Shirt.objects.create(
      brand = request.POST['brand'],
      size = request.POST['size'],
      color = request.POST['color'],
      owner = logged_in_student
    )

    return redirect("/my_profile")
