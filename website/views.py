from django.shortcuts import render
from django import views

def homePage(request):
    return render(request, 'website/index.html')
