from django.urls import path, include
from rest_framework import routers
from api.views import AlumnoView, ProfesorView, BodegueroView, AdministradorView, HerramientaView

# Versioning
router = routers.DefaultRouter()
router.register(r'Alumno', AlumnoView, 'Alumno')
router.register(r'Profesor', ProfesorView, 'Profesor')
router.register(r'Bodeguero', BodegueroView, 'Bodeguero')
router.register(r'Administrador', AdministradorView, 'Administrador')
router.register(r'Herramienta', HerramientaView, 'Herramienta')



urlpatterns = [
    path('v1/', include(router.urls)),
]
