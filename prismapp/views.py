from django.shortcuts import render, redirect, HttpResponse, Http404
from django.contrib.auth.forms import UserCreationForm
from . import forms
from django.contrib.auth.decorators import login_required


# ドライブ
@login_required
def drive(request):
    user = request.user
    form = forms.MyForm()
    d = {
        'form': form,
        'user': user
    }
    return render(request, 'drive.html', d)


# 登録
def registration(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('prism:login')
    d = {
        'form': form,
    }
    return render(request, "auth/registration.html", d)


def test(request):
    return render(request, "front_test.html")
