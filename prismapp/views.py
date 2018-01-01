from django.shortcuts import render, redirect, HttpResponse
from . import forms


# Create your views here.

def drive(request):
    form = forms.MyForm()
    return render(request, 'drive.html', {
        'form': form,
    })


def test(request):
    return render(request, "front_test.html")
