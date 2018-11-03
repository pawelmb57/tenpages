from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from tenpgs.models import *
from django.contrib.auth import authenticate
# from django.contrib.auth.forms import UserCreationForm

# Create your views here.
# def login(request):
#     email    = request.POST.get('email')
#     password = request.POST.get('password')
#     user = authenticate(request, email=email, password=password)
#
#     print(user)
#
#     if user is not None:
#         login(request, user)
#         # return render(request, 'index.html')


def signup(request):
    return render(request, '/signup/')
    # form_class = UserCreationForm
    #
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         email = form.cleaned_data.get('email')
    #         raw_password = form.cleaned_data.get('password1')
    #         user = authenticate(email=email, password=raw_password)
    #         login(request, user)
    #         return redirect('index.html')
    # else:
    #     form = UserCreationForm()
    # return render(request, '/account/login/', {'form': form})
    #
    #




def index(request):
    if request.user.is_authenticated:
        return render(request, '')

    else:
        return render(request, '/accounts/login/')





def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
