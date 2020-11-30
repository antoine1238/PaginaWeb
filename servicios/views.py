from django.shortcuts import render

from .models import Servicio

def servicios_home(request):

    servicios = Servicio.objects.all()

    return render(request,"servicios/home.html", {"servicios": servicios})