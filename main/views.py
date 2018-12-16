
from django.template.context_processors import csrf
from django.views.generic import TemplateView
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.urls import reverse
from django.contrib.auth.models import User


from main.models import Books, UserBooks, LogPages, Activity, Profile
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

    userList = User.objects.all()

    following = Profile.get_following(request.user)



    return render(request, 'main/activity.html', {
        'userList': userList,
        'following': following,
    })





def profile(request, username):

    # testset = User.objects.values()
    testset = Activity.objects.values() #filter(to_user__pk=self.pk, activity_type=Activity.FOLLOW)
    page_user = get_object_or_404(User, username=username)


    followers = Profile.get_followers(page_user)

    if request.user == page_user:
        to_follow = 'ITS YOU'
    elif request.user in followers:
        to_follow = 'Unfollow'
    else:
        to_follow = 'Follow'




    following = None
    if request.user.is_authenticated:
        following = Profile.get_following(page_user)



    return render(request, 'main/profile.html', {
        'testset': testset,
        'followers': followers,
        'following': following,
        'page_user': page_user,
        'to_follow': to_follow,
    })




def act_follow(request, username):
    print('follow beginning')

    from_user = request.user
    to_user   = get_object_or_404(User, username=username)


    following = Profile.get_following(from_user)

    if to_user not in following:
        activity = Activity(from_user=from_user, to_user=to_user, activity_type=Activity.FOLLOW)
        activity.save()

    # return HttpResponse()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def act_unfollow(request, username):
    print('unfollow beginning')

    from_user = request.user
    to_user   = get_object_or_404(User, username=username)

    following = Profile.get_following(from_user)

    if to_user in following:
        activity = Activity.objects.get(from_user=from_user, to_user=to_user, activity_type=Activity.FOLLOW)
        activity.delete()


    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
