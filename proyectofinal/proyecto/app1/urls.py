from django.urls import path
from app1.views import *

urlpatterns = [
############## REGISTRO DE USUARIO Y INICIO EN PAGINA PRINCIPAL ##############
path("inicio/",inicio,name="inicio"),
path("registro/", registro, name="registro"),
path("iniciar_sesion/",iniciar_sesion, name="iniciar_sesion"),
path("comienzo/",comienzo, name="comienzo"),
path("cerrar_sesion/",cerrar_sesion, name="cerrar_sesion"),
path("inicio_superusuario/",inicio_superusuario, name="inicio_superusuario"),

################################# CRUD #######################################

path("crear_producto/",crear_productos,name="crear_producto"),
path('producto/list/',productoList.as_view(), name='List'),
path('producto/editar/<int:pk>/',productoUpdate.as_view(),name='Edit'),
path('producto/borrar/<int:pk>/',productoDelete.as_view(),name='Delete'),

#lista de productos sin el CRUD
path('producto/listaUsuario/',listaUsuario.as_view(),name='listaUsuario'), 

################################ BUSCAR #####################################

path("buscarProducto/",buscarProducto,name="buscarProducto"),
path("resultados/",resultados, name="resutadosBusqueda"),

]