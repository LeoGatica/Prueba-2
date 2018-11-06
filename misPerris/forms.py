from django import forms


class UsuarioForm(forms.Form):
    email = forms.EmailField()
    rut = forms.CharField(max_length=10)
    nombreCompleto= forms.CharField(max_length=200)
    f_nacimiento = forms.DateTimeField()
    fono = forms.IntegerField()
    region = forms.CharField(max_length=30)
    comuna = forms.CharField(max_length=30)
    tipoVivienda = forms.CharField(max_length=30)