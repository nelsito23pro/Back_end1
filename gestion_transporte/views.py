from django.shortcuts import render
from rest_framework import viewsets

def inicio(request):
    return render(request, 'gestion_transporte/inicio.html')

# Create your views here.

# 1. Importamos todos los modelos de datos
from .models import (
    Rol, Usuario, Conductor, Vehiculo, Ruta, Parada,
    EstadoViaje, Viaje, Evento, Incidencia, Auditoria,
)

# 2. Importamos los serializadores
from .serializer import (
    RolSerializer, UsuarioSerializer, ConductorSerializer,
    VehiculoSerializer, RutaSerializer, ParadaSerializer,
    EstadoViajeSerializer, ViajeSerializer, EventoSerializer,
    IncidenciaSerializer, AuditoriaSerializer,
)


# Vista de la página de inicio (la interfaz HTML)
def inicio(request):
    return render(request, 'gestion_transporte/inicio.html')


# 3. ViewSets: cada uno entrega el CRUD completo de su modelo
#    (GET lista/detalle, POST, PUT, PATCH y DELETE)

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class ConductorViewSet(viewsets.ModelViewSet):
    queryset = Conductor.objects.all()
    serializer_class = ConductorSerializer


class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer


class RutaViewSet(viewsets.ModelViewSet):
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer


class ParadaViewSet(viewsets.ModelViewSet):
    queryset = Parada.objects.all()
    serializer_class = ParadaSerializer


class EstadoViajeViewSet(viewsets.ModelViewSet):
    queryset = EstadoViaje.objects.all()
    serializer_class = EstadoViajeSerializer


class ViajeViewSet(viewsets.ModelViewSet):
    queryset = Viaje.objects.all()
    serializer_class = ViajeSerializer


class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer


class IncidenciaViewSet(viewsets.ModelViewSet):
    queryset = Incidencia.objects.all()
    serializer_class = IncidenciaSerializer


class AuditoriaViewSet(viewsets.ModelViewSet):
    queryset = Auditoria.objects.all()
    serializer_class = AuditoriaSerializer