from django.shortcuts import render
from django.http import HttpResponse
from products.models import Products

# Create your views here.



def production(request):
#    Products.objects.create(name=name, info=info, l2=l2, user=request.user)
    prod = Products.objects.all()
    return render(
        request=request,
        template_name= 'read_products.html',
        context = {'prod': prod}
    )