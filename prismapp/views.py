from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, Http404
from django.http.response import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from . import forms
from . import models

from django.contrib.auth.decorators import login_required

import os, sys, mimetypes
import io
from O_lib import maker


# ドライブ
@login_required
def drive(request):
    # リクエストがポストでファイルが送信されているかどうか
    if request.method == 'POST' and request.FILES != {}:
        file = request.FILES["file"]

        original_file_name = file.name  # 元のファイル名
        rename_file_name = maker.make_uuid(file.name)

        file.name = rename_file_name
        form = forms.UploadFileForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            form.cleaned_data["user_id"] = request.user.id
            form.cleaned_data["ori_file_name"] = original_file_name
            form.cleaned_data["re_file_name"] = rename_file_name
            print(form.cleaned_data)
            models.UploadFileModel.objects.create(**form.cleaned_data)

        # file = request.FILES["file"]  # リクエストファイルを取得しておく
        # original_file_name = file.name  # get filename
        #
        # # ファイルネームをmake_uuid関数で新しいファイルネームを作成する
        # file.name = maker.make_uuid(file_name=file.name)
        #
        # path = os.path.join(UPLOADE_DIR, file.name)  # ファイル保存パスを設定
        # destination = open(path, "wb")  # ファイル保存
        #
        # for chunk in file.chunks():
        #     destination.write(chunk)
        #
        # insert_data = models.UploadFileModel(re_file_name=file.name, ori_file_name=original_file_name)
        # insert_data.save()

        return redirect("prism:drive")

    else:  # POST通信以外はこっち
        form = forms.UploadFileForm()
        view_file = models.UploadFileModel.objects.filter(user_id=request.user.id)  # ファイル一覧をとってくる
        view_file = [{'id': i.id, 'ori_file_name': i.ori_file_name.__str__(), "time_stamp": i.time_stamp} for i in
                     view_file]

        d = {
            "title": "drive",
            'form': form,
            'view_file': view_file
        }
        return render(request, 'drive.html', d)  # 登録


# ファイル一覧を取得
@login_required
def drive_file_get(request):
    if request.method == 'GET':
        view_file = models.UploadFileModel.objects.filter(user_id=request.user.id)  # ファイル一覧をとってくる
        view_file = [{'id': i.id,
                      'ori_file_name': i.ori_file_name.__str__(),
                      "time_stamp": i.time_stamp,
                      "re_file_name": i.re_file_name.__str__(),
                      "extension": os.path.splitext(i.ori_file_name.__str__())[1]} for i in
                     view_file]

        return JsonResponse(view_file, safe=False)
    else:
        return Http404


# ajaxでのファイル送信
@login_required
def drive_file_upload(request):
    if request.method == 'POST' and request.FILES != {}:
        file_list = request.FILES.getlist("files[]")
        for file in file_list:
            original_file_name = file.name  # 元のファイル名
            rename_file_name = maker.make_uuid(file.name)
            file.name = rename_file_name

            file_model = models.UploadFileModel()
            file_model.user = request.user
            file_model.ori_file_name = original_file_name
            file_model.re_file_name = rename_file_name
            file_model.file = file
            file_model.save()

            # form = forms.UploadFileForm(data=request.POST, files=file)
            # if form.is_valid():
            #     print(True)
            #     form.cleaned_data["user_id"] = request.user.id
            #     form.cleaned_data["ori_file_name"] = original_file_name
            #     form.cleaned_data["re_file_name"] = rename_file_name
            #     models.UploadFileModel.objects.create(**form.cleaned_data)

        view_file = models.UploadFileModel.objects.filter(user_id=request.user.id)  # ファイル一覧をとってくる
        view_file = [{'id': i.id,
                      'ori_file_name': i.ori_file_name.__str__(),
                      "time_stamp": i.time_stamp,
                      "re_file_name": i.re_file_name.__str__(),
                      "extension": os.path.splitext(i.ori_file_name.__str__())[1]
                      }
                     for i in view_file]
        return JsonResponse(view_file, safe=False)

    else:
        return Http404


def drive_file_download(request, re_file_name):
    view_file = models.UploadFileModel.objects.filter(user_id=request.user.id, re_file_name=re_file_name)

    view_file = [{"file": i.file.__str__(),
                  "ori_file_name": i.ori_file_name.__str__()
                  } for i in view_file][0]
    file_path = os.path.join(settings.MEDIA_ROOT, view_file["file"])
    print(file_path)
    # return HttpResponse(view_file)
    content = open(file_path, 'rb')
    mime = mimetypes.guess_type(file_path)
    response = HttpResponse(content, content_type=mime[0])

    response['Content-Disposition'] = 'attachment; filename="' + view_file["ori_file_name"] + '"'
    return response


######################################################################
# 認証関連
######################################################################


# 認証
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
    print(request.user)
    return render(request, "front_test.html")
