from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from . import forms
from . import models

from django.contrib.auth.decorators import login_required

import os, sys

UPLOADE_DIR = settings.MEDIA_ROOT


# ドライブ
@login_required
def drive(request):
    if request.method == 'POST':
        file = request.FILES["file"]
        path = os.path.join(UPLOADE_DIR,file.name)
        destination = open(path, "wb")

        for chunk in file.chunks():
            destination.write(chunk)

        insert_data = models.UploadFileModel(file_name = file.name)
        insert_data.save()

        return redirect("prism:drive")

    else:
        form = forms.UploadFileForm()
        d = {
            "title": "drive",
            'form': form,
        }
        return render(request, 'drive.html', d)  # 登録


def registration(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('prism:login')
    d = {
        "title": "registration",
        'form': form,
    }
    return render(request, "auth/registration.html", d)


def test(request):
    return render(request, "front_test.html")
