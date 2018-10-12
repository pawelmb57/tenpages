from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^hello/$', hello.views.index, name='index'),
    path(r'hello/login.html', hello.views.login, name='login'),
    url(r'^db', hello.views.db, name='db'),
    path('admin/', admin.site.urls),
]
