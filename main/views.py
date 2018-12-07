
from django.template.context_processors import csrf
from django.views.generic import TemplateView
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User


from main.models import Books, UserBooks, LogPages
from main.forms import AddBookForm, LogPagesForm#, AddBookUserForm

from itertools import chain




def IndexPageView(request):
    template_name = 'main/index.html'

    # def dispatch(self, request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('accounts:log_in')

    if request.method == "POST":
        form = LogPagesForm(request.user, request.POST)

        if form.is_valid():
            log = form.save(commit=False)

            log.user = request.user
            log.Books = form.cleaned_data['userbooks']
            log.log_pages = form.cleaned_data['log_pages']
            log.log_date = form.cleaned_data['log_date']
            log.save()

            return redirect('log_pages')
    else:
        form = LogPagesForm(request.user)






    return render(request, 'main/index.html', {
        'form': form,
    })




def new_book(request):
    user = request.user

    if request.method == "POST":
        form = AddBookForm(request.POST)

        if form.is_valid():
            books = form.save(commit=False)
            ub = UserBooks()

            books.book_title = form.cleaned_data['book_title']
            books.book_total_pages = form.cleaned_data['book_total_pages']
            books.save()

            ub.user = request.user
            # ub.book_title = books.book_title #books()
            ub.books = books
            ub.save()

            return redirect('new_book')
    else:
        form = AddBookForm()

    allBooks = Books.objects.values()
    userbooks = UserBooks.objects.filter(user=request.user).select_related()


    return render(request, 'main/addanewbook.html', {
        'form': form,
        'allBooks': allBooks,
        'userbooks': userbooks,
    })


def log_pages(request):

    if request.method == "POST":
        form = LogPagesForm(request.user, request.POST)

        if form.is_valid():
            log = form.save(commit=False)

            log.user = request.user
            log.Books = form.cleaned_data['userbooks']
            log.log_pages = form.cleaned_data['log_pages']
            log.save()

            return redirect('log_pages')
    else:
        form = LogPagesForm(request.user)


    # allBooks = Books.objects.all()
    logpages = LogPages.objects.select_related()
    # logpages = LogPages.objects.filter(user=request.user).select_related()

    # userlogbooks = list(chain(allBooks, logpages))



    return render(request, 'main/logpages.html', {
        'logpages': logpages,
        # 'userlogbooks': userlogbooks,
        'form': form,
    })


def log_dash(request):

    logdash = LogPages.objects.select_related()

    return render(request, 'main/logdash.html', {
        'logdash': logdash,
    })



class ChangeLanguageView(TemplateView):
    template_name = 'main/change_language.html'



def activity(request):

    userList = User.objects.values()


    return render(request, 'main/activity.html', {
        'userList': userList,
    })


def profile(request, username):
    return render(request, 'main/profile.html', {

    })
