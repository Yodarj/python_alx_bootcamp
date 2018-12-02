from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def main_page(request):
    return HttpResponse('main page')

def hello_world(request):
    return HttpResponse(content='hello world')

def hello_personalized(request, name):
    return HttpResponse(content=f'hello {name}')

