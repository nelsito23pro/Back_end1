from django.shortcuts import render

def inicio(request):
    return render(request, 'gestion_transporte/inicio.html')

# Create your views here.
