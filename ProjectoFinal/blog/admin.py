from django.contrib import admin
from blog.models import autor, articulo,seccion

# Register your models here.
admin.site.register(articulo)
admin.site.register(autor)
admin.site.register(seccion)