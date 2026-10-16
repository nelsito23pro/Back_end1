from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

#el router genera automaticmante las rutas de cas viewset

router = DefaultRouter()
router.register(r'roles', views.RolViewSet)
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'conductores', views.ConductorViewSet)
router.register(r'vehiculos', views.VehiculoViewSet)
router.register(r'rutas', views.RutaViewSet)
router.register(r'paradas', views.ParadaViewSet)
router.register(r'estados-viaje', views.EstadoViajeViewSet)
router.register(r'viajes', views.ViajeViewSet)
router.register(r'eventos', views.EventoViewSet)
router.register(r'incidencias', views.IncidenciaViewSet)
router.register(r'auditorias', views.AuditoriaViewSet)

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('api/', include(router.urls)),
]