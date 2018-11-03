from django.conf.urls import include, url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib import admin

admin.autodiscover()

from tenpgs import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('admin/', admin.site.urls),

    # url(r'^signup/$', views.signup, name='signup'),

]


urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),

]
