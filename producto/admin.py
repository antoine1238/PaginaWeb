
from django.contrib import admin

# Register your models here.

from .models import Producto, Categoria


class ProductoAdmin(admin.ModelAdmin):
    list_display = ("pk", "usuario", "nombre", "precio", "imagen", "descripcion", "created", "modified")
    
    readonly_fields = ("modified", "created")

class categoriaAdmin(admin.ModelAdmin):
    readonly_fields = ("modified", "created")

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, categoriaAdmin)
