
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.http import JsonResponse, HttpResponse

# Create your views here.
from .models import Producto, Categoria
from .forms import ProductoForm

class Home(ListView):
    template_name = "producto/home.html"
    queryset = Producto.objects.all().order_by('-created')

    context_object_name = "tienda"
    model = Producto
    

class AddProduct(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = "producto/add.html"
    success_url = reverse_lazy("tienda")
