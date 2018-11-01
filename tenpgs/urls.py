from django.conf.urls import include, url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib import admin

admin.autodiscover()

from tenpgs import views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

# urlpatterns = [
#     url(r'^hello/$', hello.views.index, name='index'),
#     path(r'hello/login.html', hello.views.login, name='login'),
#     url(r'^db', hello.views.db, name='db'),
#     path('admin/', admin.site.urls),
# ]


urlpatterns = [
    path('index.html', views.index, name='index'),

    # path('tenpgs/login.html', views.login, name='login'),
    # path('tenpgs/signup.html', views.signup, name='signup'),
    # url(r'^login/$', auth_views.LoginView.as_view(template_name="tenpgs/login.html"), name="login"),


    path('admin/', admin.site.urls),
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls'))
]
