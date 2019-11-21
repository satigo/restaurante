from django.db import models
from django.contrib import admin

#Define la clase Plato, esta tabla no se relaciona con nadie más.

class Plato(models.Model):

    nombre  =   models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nombre


#En una misma película actúan varios actores, y un actor puede actuar en varias películas.
#Por lo tanto necesitamos una relación many to many (muchos a muchos).
#Recordemos que esto no es SQL por lo tanto las reglas de normalización como tales no se
#aplican, esto es un ORM (manejo orientado a objetos), aunque internamente la BD si sea SQL



 #Aquí indicamos que la propiedad actores es del tipo Many to Many.
# Y le indicamos que se relaciona con Actor a través (through) la clase Actuación, que se define más adelante.

class Menu(models.Model):
    nombre    = models.CharField(max_length=60)   
    platos   = models.ManyToManyField(Plato, through='Asignacion')

    def __str__(self):
        return self.nombre



#Definimos la clase intermedia que se encargará de relacionar de uno a muchos Película y Actor.
#En esta definimos las llaves foraneas que nos relacionan a Actor y a Película.
# on_delete = models.CASCADE le indica que en caso de eliminar borre en cascada los datos relacionados.

class Asignacion (models.Model):
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)



#Estas clases las usamos para indicarle a la página admin que despliegue los datos relacionados en linea.
#Es decir en el mismo formulario ambas tablas.

class AsignacionInLine(admin.TabularInline):

    model = Asignacion
#muestra una linea extra al momento de insertar, como indicación al usuario que se pueden ingresar varios platos.
    extra = 1


class PlatoAdmin(admin.ModelAdmin):
    inlines = (AsignacionInLine,)


class MenuAdmin (admin.ModelAdmin):
    inlines = (AsignacionInLine,)