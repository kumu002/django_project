from hashlib import md5

from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm
from .models import Users, Parking_places


# Create your views here.
# Home page
def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        name = request.POST["name"]
        email = request.POST["email"]
        userrole = request.POST["roles"]
        password = request.POST["password"]
        confirmation = request.POST["conformpassword"]
        print(userrole)
        if password != confirmation:
            return render(request, HttpResponse('Passwords do not match'))
        else:

            user = Users.objects.create(name=name, role_id=userrole, email=email, password=password)
            user.save()

            return redirect('login')

    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = Users.objects.get(email=username)
        # user = authenticate(request, username=username, password=password)

        if password == user.password:
            request.session["user_id"] = user.id
            request.session["email"] = user.email
            request.session["name"] = user.name
            request.session["role_id"] = user.role_id
            return redirect('home2')
            # return redirect('/')
        # user = authenticate(username=username, password=password)

        else:
            # messages(request, "invalid username or password")
            return redirect('login')

    return render(request, 'login.html')


def home2(request):
    all_posts = Parking_places.objects.raw("Select * from registration_parking_places, registration_location where role_id=2")
    return render(request, "home2.html", {'all_posts': all_posts})


# logout page
def logout(request):
    del request.session
    return redirect('login')
