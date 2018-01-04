from django.shortcuts import render, redirect, HttpResponse, Http404
from django.contrib.auth.forms import UserCreationForm
from . import forms


# Create your views here.

def drive(request):
    form = forms.MyForm()
    d = {
        'form': form,
    }
    return render(request, 'drive.html', d)


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
