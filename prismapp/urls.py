from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from . import views

from django.contrib.auth.views import login, logout

login_tmp = {
    "login": "auth/login.html",
}

urlpatterns = [

    path('drive/', views.drive, name='drive'),
    path('drive_file_upload/', views.drive_file_upload, name='drive_file_upload'),
    path('drive_file_get/', views.drive_file_get, name='drive_file_get'),

    path('drive_file_download/<str:re_file_name>', views.drive_file_download, name='drive_file_download'),

    path('test/', views.test, name='test'),

    path('registration/', views.registration, name="registration"),
    path('login/', login, {'template_name': 'auth/login.html'}, name='login'),
    path('logout/', logout, {'next_page': 'prism:login'}, name='logout'),
]
