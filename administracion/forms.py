from django import forms

#Forms de las distintas clases
class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    telefono = forms.IntegerField(required=True)
    

class EmpleadoForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    oficio = forms.CharField(max_length=50, required=True)
    

class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    marca = forms.CharField(max_length=50, required=True)
    stock = forms.IntegerField(required=True)

class ProovedorForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    producto = forms.CharField(max_length=50, required=True)
     
    
    


