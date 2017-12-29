from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^drive/$', views.drive, name='drive'),
]
