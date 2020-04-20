import random

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#generator here is app and all apps should be under templates
def home(request):
    return HttpResponse(render(request,"generator/home.html"))

def password(request):
    characters=list('abcdefghijklmnopqrstuvwxyz')
    length=int(request.GET.get('length'))
    generatedpassword=''
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    for x in range(length):
        generatedpassword+=random.choice(characters)

    return HttpResponse(render(request,"generator/passwordgenerator.html",{'password': generatedpassword}))

def about(request):
    return HttpResponse(render(request,"generator/about.html"))



