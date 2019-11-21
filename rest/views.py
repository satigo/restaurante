from django.shortcuts import render
from django.contrib import messages
from .forms import MenuForm
from rest.models import Menu, Asignacion

# Create your views here.
def menu_nuevo(request):
    if request.method == "POST":
        formulario = MenuForm(request.POST)
        if formulario.is_valid():
            menu = Menu.objects.create(nombre=formulario.cleaned_data['nombre'])
            for plato_id in request.POST.getlist('platos'):
                asignacion = Asignacion(plato_id=plato_id, menu_id = menu.id)
                asignacion.save()
            messages.add_message(request, messages.SUCCESS, 'Menu Guardado Exitosamente')
    else:
        formulario = MenuForm()
    return render(request, 'rest/menu_editar.html', {'formulario': formulario})