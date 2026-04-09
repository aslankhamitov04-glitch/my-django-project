from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Hello Django on Render!</h1>")


from django.shortcuts import render

# Create your views here.
