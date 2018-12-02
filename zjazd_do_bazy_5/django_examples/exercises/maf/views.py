from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def funki(request, func, l1, l2):
    if func == 'add':
        summ = float(l1) + float(l2)
        return HttpResponse(content=summ)
    elif func == 'mul':
        mul = float(l1) * float(l2)
        return HttpResponse(content=mul)
    elif func == 'mean':
        mean = (float(l1) + float(l2))/2
        return HttpResponse(content=mean)
    elif func == 'sub':
        sub = float(l1) - float(l2)
        return HttpResponse(content=sub)
    elif func == 'div':
        div = float(l1) / float(l2)
        return HttpResponse(content=div)
    else:
        return HttpResponse(content="coś zrobiłeś źle")