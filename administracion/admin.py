from django.contrib import admin
from .models import *

class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "email", "telefono")

class ProovedorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "producto")
    
class ProductosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "marca")
    
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "oficio")

    
    

admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Proovedor,ProovedorAdmin)
admin.site.register(Productos,ProductosAdmin)
admin.site.register(Empleado, EmpleadoAdmin)


