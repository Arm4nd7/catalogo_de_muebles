from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
import random
#MODELOS
from .models import Mueble
from .models import Cliente
from .models import Compra
#FORMULARIOS
from mueblesemae.forms import MuebleForm
from mueblesemae.forms import ClienteForm
from mueblesemae.forms import CompraForm
#LOGIN
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required


#PAGINA INICIO MUEBLES
def index(request):
    muebles = Mueble.objects.all()
    template = loader.get_template('index.html')
    descripciones1 = [
            "Elegancia y conciencia ecológica en un solo mueble.",
            "Diseño moderno y sostenible, fabricado con materiales reciclados de alta calidad.",
            "Estructura resistente y ecológica, ideal para un hogar comprometido con el planeta.",
            "Un mueble funcional que combina estilo, durabilidad y responsabilidad ambiental.",
            "Elaborado con madera y materiales reciclados para reducir el impacto ambiental.",
            "Optimiza tu espacio con un diseño práctico y sustentable."
    ]
    descripcion_aleatoria1 = random.choice(descripciones1)
    descripciones2 = [
            "Elaborado con madera y materiales reciclados para reducir el impacto ambiental.",
            "Estructura resistente y ecológica, ideal para un hogar comprometido con el planeta.",
            "Diseño moderno y sostenible, fabricado con materiales reciclados de alta calidad.",
            "Un mueble funcional que combina estilo, durabilidad y responsabilidad ambiental.",
            "Optimiza tu espacio con un diseño práctico y sustentable.",
            "Elegancia y conciencia ecológica en un solo mueble."
    ]
    descripcion_aleatoria2 = random.choice(descripciones2)
    descripciones3 = [
            "Estructura resistente y ecológica, ideal para un hogar comprometido con el planeta.",
            "Diseño moderno y sostenible, fabricado con materiales reciclados de alta calidad.",
            "Un mueble funcional que combina estilo, durabilidad y responsabilidad ambiental.",
            "Optimiza tu espacio con un diseño práctico y sustentable.",
            "Elaborado con madera y materiales reciclados para reducir el impacto ambiental.",
            "Elegancia y conciencia ecológica en un solo mueble."
    ]
    descripcion_aleatoria3 = random.choice(descripciones3)
    return HttpResponse(template.render({
        'descripcion1': descripcion_aleatoria1,
        'descripcion2': descripcion_aleatoria2,
        'descripcion3': descripcion_aleatoria3,
        
        'muebles': muebles
        }, request))

##CATEGORIA ORGANIZACION
def categoria_organizacion(request):
    muebles = Mueble.objects.all()
    template = loader.get_template('categoria_organizacion.html')
    return HttpResponse(template.render({
        'muebles': muebles,
        }, request))

##CATEGORIA HOOL
def categoria_hool(request):
    muebles = Mueble.objects.all()
    template = loader.get_template('categoria_hool.html')
    return HttpResponse(template.render({
        'muebles': muebles,
        }, request))

##CATEGORIA CONFORT
def categoria_confort(request):
    muebles = Mueble.objects.all()
    template = loader.get_template('categoria_confort.html')
    return HttpResponse(template.render({
        'muebles': muebles,
        }, request))


def mueble(request, mueble_id):
    mueble =  Mueble.objects.get(id = mueble_id)
    template = loader.get_template('display_mueble.html')
    context = {
        'mueble': mueble
    }
    return HttpResponse(template.render(context, request))

#PAGINA CLIENTE
def clientes(request):    
    clientes = Cliente.objects.all()
    template = loader.get_template('cliente_list.html')
    return HttpResponse(template.render({'clientes': clientes}, request))

#TABLA CLIENTE
def cliente_tabla(request):    
    clientes = Cliente.objects.all()
    template = loader.get_template('cliente_tabla.html')
    return HttpResponse(template.render({'clientes': clientes}, request))

def cliente_details(request, cliente_id):
    cliente = Cliente.objects.get(id = cliente_id)
    template = loader.get_template('display_cliente.html')
    context = {
        'cliente': cliente
    }
    return HttpResponse(template.render(context, request))

#EDICIONES CLIENTE
@login_required
def add_cliente(request):
    if request.method == "POST": 
        form = ClienteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mueblesemae:clientes')
    else:
        form = ClienteForm()        
    return render(request, 'cliente_form.html', {'form': form})

def edit_cliente(request, cliente_id):
    cliente =  Cliente.objects.get(id = cliente_id)
    if request.method == "POST": 
        form = ClienteForm(request.POST, request.FILES, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('mueblesemae:clientes')
    else:
        form = ClienteForm(instance=cliente)   
    return render(request, 'cliente_form.html', {'form': form})

def delete_cliente(request, cliente_id):
    cliente =  Cliente.objects.get(id = cliente_id)
    cliente.delete()
    return redirect('mueblesemae:clientes')


#EDICIONES MUEBLE
@login_required
def add_mueble(request):
    if request.method == "POST": 
        form = MuebleForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('mueblesemae:index')
    else:
        form = MuebleForm()        
    return render(request, 'mueble_form.html', {'form': form})

def edit_mueble(request, mueble_id):
    mueble =  Mueble.objects.get(id = mueble_id)
    if request.method == "POST": 
        form = MuebleForm(request.POST, request.FILES, instance=mueble)
        if form.is_valid():
            form.save()
            return redirect('mueblesemae:index')
    else:
        form = MuebleForm(instance=mueble)   
    return render(request, 'mueble_form.html', {'form': form})

def delete_mueble(request, mueble_id):
    mueble =  Mueble.objects.get(id = mueble_id)
    mueble.delete()
    return redirect('mueblesemae:index')


#Compras
def listar_compras(request):
    compras = Compra.objects.all().order_by('-fecha')
    template = loader.get_template('lista_compras.html')
    return HttpResponse(template.render({'compras': compras}, request))


#Nueva compra
def ingresar_compra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            compra = form.save()
            compra.calcular_total()
            return redirect('mueblesemae:listar_compras')
    else:
        form = CompraForm()
    
    return render(request, 'ingresar_compra.html', {'form': form})

#Detalle compra
def detalle_compra(request, cliente_id, compra_id):
    cliente = Cliente.objects.get(id=cliente_id)
    compra = Compra.objects.get(id=compra_id, cliente=cliente)  # Obtiene solo la compra específica
    return render(request, 'detalle_compra.html', {
        'cliente': cliente,
        'compra': compra,
    })

#login creado
class CustomLoginView(LoginView):
    template_name = "login_form.html"