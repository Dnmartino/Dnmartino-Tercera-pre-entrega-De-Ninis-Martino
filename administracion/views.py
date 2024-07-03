from django.shortcuts import render
from .models import *
from .forms import *

# Funciones botones principales

def home(request):
    return render(request, "administracion/index.html")

def clientes(request):
    contexto = {"clientes": Cliente.objects.all()}
    return render(request, "administracion/clientes.html",contexto)

def empleados(request):
    contexto = {"empleados": Empleado.objects.all()}
    return render(request, "administracion/empleados.html", contexto)

def proovedores(request):
    contexto = {"proovedores": Proovedor.objects.all()}
    return render(request, "administracion/proovedores.html", contexto)

def productos(request):
    contexto = {"productos": Productos.objects.all()}
    return render(request, "administracion/productos.html", contexto)

def acerca(request):
    return render(request,"administracion/acerca.html")

def contacto(request):
    return render(request,"administracion/contacto.html")


#Formularios_______________________________________________


def clienteForm(request):
    if request.method == "POST":
        formcliente = ClienteForm(request.POST)
        if formcliente.is_valid():
            cliente_nombre = formcliente.cleaned_data.get("nombre")
            cliente_apellido = formcliente.cleaned_data.get("apellido")
            cliente_email = formcliente.cleaned_data.get("email")
            cliente_telefono = formcliente.cleaned_data.get("telefono")
            cliente = Cliente(nombre=cliente_nombre, apellido=cliente_apellido, email=cliente_email,telefono=cliente_telefono)
            cliente.save()
            contexto = {"clientes": Cliente.objects.all()}
            return render(request, "administracion/clientes.html",contexto)
    else:
         formcliente= ClienteForm()
        
    return render(request, "administracion/clienteform.html", {"form":formcliente})

def empleadoForm(request):
    if request.method == "POST":
        formempleado = EmpleadoForm(request.POST)
        if formempleado.is_valid():
            empleado_nombre = formempleado.cleaned_data.get("nombre")
            empleado_apellido = formempleado.cleaned_data.get("apellido")
            empleado_oficio = formempleado.cleaned_data.get("oficio")
            empleado = Empleado(nombre=empleado_nombre, apellido=empleado_apellido, oficio=empleado_oficio)
            empleado.save()
            contexto = {"empleados": Empleado.objects.all()}
            return render(request, "administracion/empleados.html",contexto)
    else:
         formempleado= EmpleadoForm()
        
    return render(request, "administracion/empleadoform.html",{"form":formempleado})

def productoForm(request):
    if request.method == "POST":
        formproducto = ProductoForm(request.POST)
        if formproducto.is_valid():
            producto_nombre = formproducto.cleaned_data.get("nombre")
            producto_marca = formproducto.cleaned_data.get("marca")
            producto_stock = formproducto.cleaned_data.get("stock")
            producto = Productos(nombre=producto_nombre, marca=producto_marca, stock=producto_stock)
            producto.save()
            contexto = {"productos": Productos.objects.all()}
            return render(request, "administracion/productos.html",contexto)
    else:
         formproducto= ProductoForm()
        
    return render(request, "administracion/productoform.html",{"form":formproducto})

def proovedorForm(request):
    if request.method == "POST":
        formproovedor = ProovedorForm(request.POST)
        if formproovedor.is_valid():
            proovedor_nombre = formproovedor.cleaned_data.get("nombre")
            proovedor_producto = formproovedor.cleaned_data.get("producto")
            proovedor = Proovedor(nombre=proovedor_nombre,producto=proovedor_producto)
            proovedor.save()
            contexto = {"proovedores": Proovedor.objects.all()}
            return render(request, "administracion/proovedores.html",contexto)
    else:
         formproovedor= ProovedorForm()
        
    return render(request, "administracion/proovedorform.html",{"form":formproovedor})


def BuscarProductos(request):
    return render(request,"administracion/buscarproductos.html")

def EncontrarProductos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        productos = Productos.objects.filter(nombre__icontains=patron)
        contexto = {'productos': productos}    
    else:
        contexto = {'productos': Productos.objects.all()}
        
    return render(request, "administracion/productos.html", contexto)