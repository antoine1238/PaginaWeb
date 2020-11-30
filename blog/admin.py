""" Django."""
from django.contrib import admin


""" Local."""
from .models import Categoria, Post


class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ("id","created", "updated")
    list_display=("id","titulo", "contenido", "created", "updated")
    search_fields=["titulo"]

    
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)