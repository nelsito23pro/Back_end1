from django.db import models

# Create your models here.

# 1. ROL
class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200, blank=True)

    class Meta:
        db_table = 'rol'
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.nombre


# 2. USUARIO
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=255)
    estado = models.BooleanField(default=True)
    id_rol = models.ForeignKey(Rol, on_delete=models.PROTECT, db_column='id_rol')

    class Meta:
        db_table = 'usuario'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


# 3. CONDUCTOR
class Conductor(models.Model):
    ESTADOS = [
        ('DISPONIBLE', 'Disponible'),
        ('NO_DISPONIBLE', 'No disponible'),
    ]

    id_conductor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rut = models.CharField(max_length=20, unique=True)
    numero_licencia = models.CharField(max_length=50)
    tipo_licencia = models.CharField(max_length=20)
    fecha_vencimiento_licencia = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='DISPONIBLE')

    class Meta:
        db_table = 'conductor'
        verbose_name = 'Conductor'
        verbose_name_plural = 'Conductores'

    def __str__(self):
        return f'{self.nombre} {self.apellido} ({self.rut})'


# 4. VEHICULO
class Vehiculo(models.Model):
    ESTADOS = [
        ('DISPONIBLE', 'Disponible'),
        ('VIAJE', 'En viaje'),
        ('MANTENCION', 'En mantención'),
    ]

    id_vehiculo = models.AutoField(primary_key=True)
    patente = models.CharField(max_length=10, unique=True)
    tipo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField(db_column='año')
    capacidad = models.IntegerField()
    kilometraje = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=30, choices=ESTADOS, default='DISPONIBLE')

    class Meta:
        db_table = 'vehiculo'
        verbose_name = 'Vehículo'
        verbose_name_plural = 'Vehículos'

    def __str__(self):
        return self.patente


# 5. RUTA
class Ruta(models.Model):
    ESTADOS = [
        ('ACTIVA', 'Activa'),
        ('INACTIVA', 'Inactiva'),
    ]

    id_ruta = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    origen = models.CharField(max_length=150)
    destino = models.CharField(max_length=150)
    distancia_km = models.DecimalField(max_digits=10, decimal_places=2)
    duracion_estimada = models.IntegerField(help_text='Duración estimada en minutos')
    estado = models.CharField(max_length=20, choices=ESTADOS, default='ACTIVA')

    class Meta:
        db_table = 'ruta'
        verbose_name = 'Ruta'
        verbose_name_plural = 'Rutas'

    def __str__(self):
        return f'{self.nombre} ({self.origen} → {self.destino})'


# 6. PARADA
class Parada(models.Model):
    id_parada = models.AutoField(primary_key=True)
    id_ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE, db_column='id_ruta', related_name='paradas',verbose_name='Ruta')
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    orden = models.IntegerField()
    hora_estimada = models.TimeField()

    class Meta:
        db_table = 'parada'
        verbose_name = 'Parada'
        verbose_name_plural = 'Paradas'
        ordering = ['id_ruta', 'orden']

    def __str__(self):
        return f'{self.nombre} (orden {self.orden})'


# 7. ESTADO_VIAJE
class EstadoViaje(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200, blank=True)
    # Ejemplos de valores: PROGRAMADO, ASIGNADO, EN_CURSO, FINALIZADO, CANCELADO, SUSPENDIDO

    class Meta:
        db_table = 'estado_viaje'
        verbose_name = 'Estado de viaje'
        verbose_name_plural = 'Estados de viaje'

    def __str__(self):
        return self.nombre


# 8. VIAJE
class Viaje(models.Model):
    id_viaje = models.AutoField(primary_key=True)
    id_ruta = models.ForeignKey(Ruta, on_delete=models.PROTECT, db_column='id_ruta')
    id_conductor = models.ForeignKey(Conductor, on_delete=models.PROTECT, db_column='id_conductor')
    id_vehiculo = models.ForeignKey(Vehiculo, on_delete=models.PROTECT, db_column='id_vehiculo')
    id_estado = models.ForeignKey(EstadoViaje, on_delete=models.PROTECT, db_column='id_estado')
    fecha_viaje = models.DateField()
    hora_salida_programada = models.TimeField()
    hora_salida_real = models.TimeField(null=True, blank=True)
    hora_llegada_programada = models.TimeField()
    hora_llegada_real = models.TimeField(null=True, blank=True)
    observaciones = models.TextField(blank=True)

    class Meta:
        db_table = 'viaje'
        verbose_name = 'Viaje'
        verbose_name_plural = 'Viajes'
        ordering = ['-fecha_viaje', 'hora_salida_programada']

    def __str__(self):
        return f'Viaje {self.id_viaje} - {self.id_ruta} ({self.fecha_viaje})'


# 9. EVENTO
class Evento(models.Model):
    id_evento = models.AutoField(primary_key=True)
    id_viaje = models.ForeignKey(Viaje, on_delete=models.CASCADE, db_column='id_viaje', related_name='eventos')
    id_usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, db_column='id_usuario')
    tipo_evento = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    estado_anterior = models.CharField(max_length=30, blank=True)
    estado_nuevo = models.CharField(max_length=30, blank=True)

    class Meta:
        db_table = 'evento'
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['-fecha_hora']

    def __str__(self):
        return f'{self.tipo_evento} - Viaje {self.id_viaje_id}'


# 10. INCIDENCIA
class Incidencia(models.Model):
    GRAVEDAD = [
        ('BAJA', 'Baja'),
        ('MEDIA', 'Media'),
        ('ALTA', 'Alta'),
        ('CRITICA', 'Crítica'),
    ]

    id_incidencia = models.AutoField(primary_key=True)
    id_viaje = models.ForeignKey(Viaje, on_delete=models.CASCADE, db_column='id_viaje', related_name='incidencias')
    id_usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, db_column='id_usuario')
    tipo = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)
    gravedad = models.CharField(max_length=20, choices=GRAVEDAD, default='BAJA')
    fecha_hora = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=30, default='ABIERTA')

    class Meta:
        db_table = 'incidencia'
        verbose_name = 'Incidencia'
        verbose_name_plural = 'Incidencias'
        ordering = ['-fecha_hora']

    def __str__(self):
        return f'{self.tipo} - {self.gravedad}'


# 11. AUDITORIA
class Auditoria(models.Model):
    ACCIONES = [
        ('INSERT', 'Insertar'),
        ('UPDATE', 'Actualizar'),
        ('DELETE', 'Eliminar'),
        ('LOGIN', 'Inicio de sesión'),
    ]

    id_auditoria = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, db_column='id_usuario')
    tabla_afectada = models.CharField(max_length=50)
    id_registro = models.IntegerField(null=True, blank=True)
    accion = models.CharField(max_length=30, choices=ACCIONES)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    detalle = models.TextField(blank=True)

    class Meta:
        db_table = 'auditoria'
        verbose_name = 'Auditoría'
        verbose_name_plural = 'Auditorías'
        ordering = ['-fecha_hora']

    def __str__(self):
        return f'{self.accion} en {self.tabla_afectada} por usuario {self.id_usuario_id}'
    
    