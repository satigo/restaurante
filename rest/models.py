from django.db import models
from django.contrib import admin

class Plato(models.Model):

    nombre  =   models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nombre


class Menu(models.Model):
    nombre    = models.CharField(max_length=60)   
    platos   = models.ManyToManyField(Plato, through='Asignacion')

    def __str__(self):
        return self.nombre



class Asignacion (models.Model):
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)


class AsignacionInLine(admin.TabularInline):

    model = Asignacion
    extra = 1


class PlatoAdmin(admin.ModelAdmin):
    inlines = (AsignacionInLine,)


class MenuAdmin (admin.ModelAdmin):
    inlines = (AsignacionInLine,)