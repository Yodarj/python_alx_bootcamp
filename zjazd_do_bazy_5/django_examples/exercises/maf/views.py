from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from maf.models import Math
from django.shortcuts import render


# Create your views here.


def funki(request, func, l1, l2):
    if request.user:
        Math.objects.create(func=func, l1=l1, l2=l2, user=request.user)
    else:
        Math.objects.create(func=func, l1=l1, l2=l2)
    return HttpResponse(calculate(func, l1, l2))


def calculate(func, l1, l2):
    result = None
    if func == 'add':
        result = float(l1) + float(l2)
    elif func == 'mul':
        result = float(l1) * float(l2)
    elif func == 'mean':
        result = (float(l1) + float(l2)) / 2
    elif func == 'sub':
        result = float(l1) - float(l2)
    elif func == 'div':
        result = float(l1) / float(l2)
    else:
        return 'x'
    return result

@login_required()
def maf_list(request):
    objects = Math.objects.all()

    out = ''
    for o in objects:
        out += f'{o.func}: {o.l1}: {o.l2} <br>'

    return render(
        request=request,
        template_name= 'maf_lists.html',
        context = {'mafs': objects}
    )


def maf_details(request, id):
    m = Math.objects.get(pk=id)

    out = f'''
Operacja: {m.func}<br>
------------------<br>
Argument 1: {m.l1}<br>
------------------<br>
Argument 2: {m.l2}<br>
------------------<br>
Wynik: {calculate(m.func, m.l1, m.l2)}
    '''

    return render(
        request=request,
        template_name='maf_details.html',
        context = {
            'maf_det': m,
            'wynik':calculate(m.func, m.l1, m.l2)}
    )
