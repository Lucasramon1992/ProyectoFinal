from django.shortcuts import render
from django.http import HttpResponse
from app1.models import *
from app1.forms import *
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

################ REGISTRO Y PAGINA DE INICIO ####################

def inicio (request):
    return render (request,"app1/inicio.html")
    
def comienzo (request):
    return render (request,"app1/registro/comienzo.html")

def registro(request):
    if request.method == "POST":
        miFormulario=UserCreationForm(request.POST)
        if miFormulario.is_valid():
            miFormulario.save()
        return render(request, "app1/inicio.html")
    else:
        miFormulario=UserCreationForm()
        return render(request, "app1/registro/registro.html", {"miFormulario":miFormulario})

def iniciar_sesion(request):
    if request.method =="POST":
        miFomulario=AuthenticationForm(request,data=request.POST)
        if miFomulario.is_valid():
            usuario=miFomulario.cleaned_data.get("username")
            contra=miFomulario.cleaned_data.get("password")
            if usuario == "admin" and contra=="administrador":
                return render(request,"app1/inicio_superusuario.html")  
           
            miUsuario= authenticate(username=usuario, password=contra)   
            if miUsuario:
                login(request, miUsuario)           
                return render(request,"app1/inicio.html",) 
            
        else:           
            return render(request,"app1/registro/comienzo.html")
    else:        
        miFomulario=AuthenticationForm()
        return render(request, "app1/registro/iniciar_sesion.html", {"miFormulario":miFomulario})


def cerrar_sesion(request):
    return render (request,"app1/registro/comienzo.html")


def inicio_superusuario(request):
    return render (request,"app1/inicio_superusuario.html")


######## LISTA DE PRODUCTOS SIN EL CRUD ########
class listaUsuario (ListView):
    model=models_producto
    template_name="app1/producto_lista_usuario.html"



################ CRUD ####################


class productoList (ListView):
    model=models_producto
    template_name="app1/producto_list.html"
    


def crear_productos (request):
    if request.method == 'POST':
        miFormulario=productosFormulario(request.POST)
        if miFormulario.is_valid():
            infoDic=miFormulario.cleaned_data
            productos1=models_producto(nombre=infoDic["nombre"], precio=infoDic["precio"])
            productos1.save()
            return render(request, "app1/productos/crear_producto.html")
    else:
        miFormulario = productosFormulario()
    return render (request, "app1/productos/crear_producto.html",{"miFormulario": miFormulario})


class productoUpdate(UpdateView):
    model=models_producto
    success_url="/app1/producto/list"
    fields=['nombre', 'precio']

class productoDelete(DeleteView):
      model=models_producto
      success_url="/app1/producto/list"



################ BUSCAR ####################

def buscarProducto(request):
   return render(request, "app1/buscar/buscarProducto.html")

def resultados(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        productos=models_producto.objects.filter(nombre__icontains=nombre)
        return render(request, "app1/buscar/resultados.html", {"productos":productos,"nombre": nombre})
    
    else:
        respuesta='no enviaste datos'
    return HttpResponse (respuesta)


