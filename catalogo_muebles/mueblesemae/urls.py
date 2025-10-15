from django.urls import path
#impotamos viewa
from . import views
app_name = 'mueblesemae'

urlpatterns = [
    path("", views.index, name="index"),
    #categorias
    path("categoria_organizacion/", views.categoria_organizacion, name="categoria_organizacion"),
    path("categoria_hool/", views.categoria_hool, name="categoria_hool"),
    path("categoria_confort/", views.categoria_confort, name="categoria_confort"),
    #clientes
    path("clientes/", views.clientes, name="clientes"),
    path("cliente_tabla/", views.cliente_tabla, name="cliente_tabla"),
    path("cliente/<int:cliente_id>/", views.cliente_details, name="cliente_details"),
    #muebles
    path("<int:mueble_id>/", views.mueble, name="mueble"),
    path("add_mueble/", views.add_mueble, name="add_mueble"),
    path("edit_mueble/<int:mueble_id>/", views.edit_mueble, name="edit_mueble"),
    path("delete_mueble/<int:mueble_id>/", views.delete_mueble, name="delete_mueble"),
    #clientes-edicion
    path("add_cliente/", views.add_cliente, name="add_cliente"),
    path("edit_cliente/<int:cliente_id>/", views.edit_cliente, name="edit_cliente"),
    path("delete_cliente/<int:cliente_id>/", views.delete_cliente, name="delete_cliente"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    #compras
    path("ingresar_compra/", views.ingresar_compra, name="ingresar_compra"),
    path("listar_compras/", views.listar_compras, name="listar_compras"),
    #DETALLE COMPRA
    path('detalle_compra/<int:cliente_id>/<int:compra_id>/', views.detalle_compra, name='detalle_compra'),
    
    
    
]

