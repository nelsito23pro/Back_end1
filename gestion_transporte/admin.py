from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import (
    Rol, Usuario, Conductor, Vehiculo, Ruta, Parada,
    EstadoViaje, Viaje, Evento, Incidencia, Auditoria,
)


@admin.register(Conductor)
class ConductorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'rut', 'tipo_licencia',
                    'fecha_vencimiento_licencia', 'estado')
    list_filter = ('estado', 'tipo_licencia')
    search_fields = ('nombre', 'apellido', 'rut')


@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('patente', 'tipo', 'marca', 'modelo', 'capacidad', 'estado')
    list_filter = ('estado', 'tipo', 'marca')
    search_fields = ('patente', 'marca', 'modelo')


@admin.register(Ruta)
class RutaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'origen', 'destino', 'distancia_km', 'estado')
    list_filter = ('estado',)
    search_fields = ('nombre', 'origen', 'destino')


@admin.register(Viaje)
class ViajeAdmin(admin.ModelAdmin):
    list_display = ('id_viaje', 'id_ruta', 'id_conductor', 'id_vehiculo',
                    'id_estado', 'fecha_viaje')
    list_filter = ('id_estado', 'fecha_viaje')
    date_hierarchy = 'fecha_viaje'


@admin.register(Incidencia)
class IncidenciaAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'gravedad', 'estado', 'id_viaje', 'fecha_hora')
    list_filter = ('gravedad', 'estado')


# Modelos simples: registro directo
admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(Parada)
admin.site.register(EstadoViaje)
admin.site.register(Evento)
admin.site.register(Auditoria)