from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from misPerris.models import Usuario
from misPerris.forms import UsuarioForm

def Principal(request):
    return render(request, 'misPerris/Principal.html', {})

def formulario(request):
    return render(request, 'misPerris/formulario.html', {})

def contactanos(request):
    return render(request, 'misPerris/contactanos.html', {}) 

def servicios(request):
    return render(request, 'misPerris/servicios.html', {}) 

def somos(request):
    return render(request, 'misPerris/somos.html', {})   

def adopcion(request):
    return render(request, 'misPerris/adopcion.html', {})    



def prueba(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        email = form_data.get("email")
        nombreCompleto = form_data.get("nombreCompleto")

        obj = UsuarioForm.objects.create(email=email, nombreCompleto=nombreCompleto)

    context = {
        "prueba" : form,
    }    
    return render(request, "formulario.html", context)




	

            
            
            
        

#def Principalito(request):
#   return render(request, 'misPerris/formulario/Principal.html', {}) 



# Create your views here.