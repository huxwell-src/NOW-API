from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Alumno, Bodeguero, Profesor, Administrador, Herramienta
from .serializers import AlumnoSerializer, BodegueroSerializer, ProfesorSerializer, AdministradorSerializer, HerramientaSerializer

class AlumnoView(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

class BodegueroView(viewsets.ModelViewSet):
    queryset = Bodeguero.objects.all()
    serializer_class = BodegueroSerializer
    
class ProfesorView(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

class AdministradorView(viewsets.ModelViewSet):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer       

class HerramientaView(viewsets.ModelViewSet):
    queryset = Herramienta.objects.all()
    serializer_class = HerramientaSerializer
    
