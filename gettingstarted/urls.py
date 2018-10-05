from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views


urlpatterns = [
    path(r'^', hello.views.index, name='index'),
    path(r'^db', hello.views.db, name='db'),
    path('admin/', admin.site.urls),
]
