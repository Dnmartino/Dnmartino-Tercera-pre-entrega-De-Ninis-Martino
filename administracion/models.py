from django.db import models
#Clases con sus respectivos models,strs y Meta.

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    oficio = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre}, {self.apellido}"
    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ["nombre"]

class Cliente(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()
    telefono = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre}, {self.apellido}"
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["nombre"]

class Productos(models.Model):
    nombre = models.CharField(max_length=60)
    marca = models.CharField(max_length=50)
    stock = models.IntegerField()
    def __str__(self):
        return f"{self.nombre}, {self.marca}"
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["nombre"]
    

class Proovedor(models.Model):
    nombre = models.CharField(max_length=50)
    producto = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre}, {self.producto}"
    
    class Meta:
        verbose_name = "Proovedor"
        verbose_name_plural = "Proovedores"
        ordering = ["nombre"]
    
    

    

