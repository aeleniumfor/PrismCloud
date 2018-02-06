from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from . import forms
from . import models

from django.contrib.auth.decorators import login_required

import os, sys
from O_lib import maker

UPLOADE_DIR = settings.MEDIA_ROOT


# ドライブ
@login_required
def drive(request):
    # リクエストがポストでファイルが送信されているかどうか
    if request.method == 'POST' and request.FILES != {}:

        file = request.FILES["file"]  # リクエストファイルを取得しておく
        original_file_name = file.name  # get filename

        # ファイルネームをmake_uuid関数で新しいファイルネームを作成する
        file.name = maker.make_uuid(file_name=file.name)

        path = os.path.join(UPLOADE_DIR, file.name)
        destination = open(path, "wb")

        for chunk in file.chunks():
            destination.write(chunk)

        insert_data = models.UploadFileModel(re_file_name=file.name, ori_file_name=original_file_name)
        insert_data.save()

        return redirect("prism:drive")

    else:  # POST通信以外はこっち
        form = forms.UploadFileForm()
        view_file = models.UploadFileModel.objects.all()  # ファイル一覧をとってくる
        view_file = [{'id': i.id, 'ori_file_name': i.ori_file_name.__str__()} for i in view_file]

        d = {
            "title": "drive",
            'form': form,
            'view_file': view_file
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
