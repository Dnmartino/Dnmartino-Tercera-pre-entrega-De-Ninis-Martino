from django.urls import path, include
from administracion.views import *
urlpatterns = [
    #urls botones de arriba
    path('', home, name="home"), 
    path('clientes', clientes, name="clientes"),
    path('empleados', empleados, name="empleados"),  
    path('productos', productos, name="productos"),  
    path('proovedores', proovedores, name="proovedores"),
    path('acerca', acerca, name="acerca"),
    path('contacto', contacto, name="contacto"), 
    
    
    #formularios de las clases
    path('clienteform', clienteForm, name="clienteform"),
    path('empeladoform', empleadoForm, name="empleadoform"),
    path('productoform', productoForm, name="productoform"),
    path('proovedorform', proovedorForm, name="proovedorform"), 
    
    
    
    
    #formulario para buscar
    path('buscarproductos', BuscarProductos, name="buscarproductos"),
    path('encontrarproductos', EncontrarProductos, name="encontrarproductos"),  
]