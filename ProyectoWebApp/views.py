from django.shortcuts import HttpResponse
from django.shortcuts import render
from servicios.models import servicios

def inicio(request):

    return render(request, "index.html")

def servicioss(request):
    
    serv=servicios.objects.all()
    return render(request, "servicios.html", {"serv":serv})

def tienda(request):

    return render(request, "tienda.html")

def blog(request):

    return render(request, "blog.html")

def contacto(request):

    return render(request, "contact.html")
