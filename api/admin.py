from django.contrib import admin
from .models import EstadoSolicitud, Alumno, Profesor, Administrador, Bodeguero, Herramienta, Solicitud, SolicitudAlumno, SolicitudHerramienta

admin.site.register(EstadoSolicitud)
admin.site.register(Alumno)
admin.site.register(Profesor)
admin.site.register(Administrador)
admin.site.register(Bodeguero)
admin.site.register(Herramienta)
admin.site.register(Solicitud)
admin.site.register(SolicitudAlumno)
admin.site.register(SolicitudHerramienta)
