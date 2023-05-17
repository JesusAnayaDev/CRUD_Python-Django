from django.shortcuts import render, redirect
from .models import Producto
from django.contrib import messages

# Create your views here.

def home(request):
    productos = Producto.objects.all()
    messages.success(request, '¡Productos listados!')
    return render(request, "gestionProductos.html", {"productos": productos})

def registrarProducto(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    cantidad=request.POST['numCantidad']

    producto=Producto.objects.create(codigo=codigo, nombre=nombre, cantidad=cantidad)
    messages.success(request, '¡Producto registrado!')
    return redirect('/')

def edicionProducto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    return render(request, "edicionProducto.html", {"producto":producto})

def editarProducto(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    cantidad=request.POST['numCantidad']

    producto = Producto.objects.get(codigo=codigo)
    producto.nombre = nombre
    producto.cantidad = cantidad
    producto.save()

    messages.success(request, '¡Producto actualizado!')

    return redirect('/')

def eliminarProducto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()

    messages.success(request, '¡Producto eliminado!')

    return redirect('/')