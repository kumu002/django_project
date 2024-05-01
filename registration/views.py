from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm
from .models import Users


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
            return HttpResponse("You're logged in.")
            # return redirect('/')
        # user = authenticate(username=username, password=password)

        else:
            # messages(request, "invalid username or password")
            return redirect('login')

    return render(request, 'login.html')

def home2(request):

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')
