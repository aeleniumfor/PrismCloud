from django.shortcuts import render, redirect, HttpResponse


# Create your views here.

def drive(request):
    d = {}
    return render(request,"drive.html")

def test(request):
    return render(request,"front_test.html")
