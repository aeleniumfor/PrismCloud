from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from . import views

from django.contrib.auth.views import login, logout

login_tmp = {
    "login": "auth/login.html",
}

urlpatterns = [

    url(r'^drive/$', views.drive, name='drive'),
    url(r'^drive_file_upload/$', views.drive_file_upload, name='drive_file_upload'),

    url(r'^test/$', views.test, name='test'),

    url(r'^registration/$', views.registration, name="registration"),
    url(r'^login/$', login, {'template_name': 'auth/login.html'}, name='login'),
    url(r'^logout/$', logout, name='logout'),
]
