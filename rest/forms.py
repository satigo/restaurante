from django import forms
from .models import Menu, Plato


class MenuForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Menu
        fields = ('nombre', 'platos')

    def __init__ (self, *args, **kwargs):
        super(MenuForm, self).__init__(*args, **kwargs)
        self.fields["platos"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["platos"].help_text = "Seleccione los Platos que integraran el menu"
        self.fields["platos"].queryset = Plato.objects.all()