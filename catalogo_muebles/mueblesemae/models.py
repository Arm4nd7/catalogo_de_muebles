from django.db import models
from django.db.models import  Q

# Create your models here.

##MUEBLES    
class Mueble(models.Model):
    name = models.CharField(max_length=15, null=False)
    MUEBLE_MATERIALS = (
        ('M', 'Madera Sostenible'),
        ('B', 'Bambú'),
        ('E', 'Eco-plásticos'),
        ('C', 'Corcho'),
        ('L', 'Lino Orgánico'),
        ('F', 'Fibras de Coco'),    
    )
    material = models.CharField(max_length=30, null=False, choices=MUEBLE_MATERIALS)
    MUEBLE_STYLES = (
        ('M', 'Minimalista'),
        ('M', 'Multifuncionales'),
        ('S', 'Sostenibles'),
        ('I', 'Industrial'),
    )
    style = models.CharField(max_length=30, null = False, choices = MUEBLE_STYLES)
    cost = models.DecimalField(decimal_places = 2, max_digits = 6, null=False, default=0)
    picture = models.ImageField(upload_to="muebles_images")
    MUEBLE_TYPE = (
        ('O', 'Organización'),
        ('H', 'Hool'),
        ('C', 'Confort'),   
    )
    type = models.CharField(max_length=30, null=False, choices=MUEBLE_TYPE)
    
    def __str__(self):
        return self.name

class Cliente(models.Model):
    name = models.CharField(max_length=15, null=False)
    last_name = models.CharField(max_length=15, null=False)
    dni = models.IntegerField(null=False, unique=True)
    email = models.EmailField(max_length=50, null=True) 
    #genero
    CLIENTE_GENDER = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    gender = models.CharField(max_length=15, null=False, choices=CLIENTE_GENDER)
    
    def __str__(self):
        return self.name + " " + self.last_name
    
#tabla compra relacional
class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField()
    muebles = models.ManyToManyField(Mueble)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def calcular_total(self):
        total = sum(mueble.cost for mueble in self.muebles.all())
        self.total = total
        self.save()
    
    def __str__(self):
        return f"Compra {self.id} - {self.muebles.name}"
    
    
    
    
    
    
