from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    # return render(request, 'index.html')
    if not request.user.is_authenticated:
        return redirect('login.html')
    else:
        return render(request, 'index.html')



def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})


def login(request):

    return render(request, 'login.html')
