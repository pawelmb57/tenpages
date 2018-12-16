from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin


from main.views import IndexPageView, ChangeLanguageView, new_book, log_pages, log_dash, activity, profile, act_unfollow, act_follow


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexPageView, name='index'),

    path('i18n/', include('django.conf.urls.i18n')),
    path('language/', ChangeLanguageView.as_view(), name='change_language'),

    path('accounts/', include('accounts.urls')),
]



urlpatterns += [
    path('newbook/', new_book, name='new_book'),
    path('logpages/', log_pages, name='log_pages'),
    path('logdash/', log_dash, name='log_dash'),

    path('activity/', activity, name='activity'),

    # url(r'^(?P<username>[^/]+)/activity/$', activity, name='activity'),
    url(r'^(?P<username>[^/]+)/$', profile, name='profile'),

    url(r'^(?P<username>[^/]+)/act_unfollow/$', act_unfollow, name='act_unfollow'),
    url(r'^(?P<username>[^/]+)/act_follow/$', act_follow, name='act_follow'),



]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
