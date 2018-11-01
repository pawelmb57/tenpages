from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from tenpgs.models import *
from django.contrib.auth import authenticate

# Create your views here.
def login(request):
    email    = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(request, email=email, password=password)

    print(user)

    if user is not None:
        login(request, user)
        # return render(request, 'index.html')



def index(request):

    if request.user.is_authenticated:
        return render(request, 'index.html')

    else:
        return render(request, 'login.html')





def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})




def signup(request):
    return render(request, 'signup.html')
