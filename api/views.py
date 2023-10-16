from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Alumno, Bodeguero, Profesor, Administrador, Herramienta
from .serializers import AlumnoSerializer, BodegueroSerializer, ProfesorSerializer, AdministradorSerializer, HerramientaSerializer, UsuarioSerializer

class UsuarioView(APIView):
    def get(self, request):
        usuarios = []

        # Obtener datos de Alumnos
        alumnos = Alumno.objects.all()
        for alumno in alumnos:
            usuarios.append({
                'email': alumno.email,
                'contrasena': alumno.contrasena,
                'rol': 'alumno'
            })

        # Obtener datos de Profesores
        profesores = Profesor.objects.all()
        for profesor in profesores:
            usuarios.append({
                'email': profesor.email,
                'contrasena': profesor.contrasena,
                'rol': 'profesor'
            })

        # Obtener datos de Administradores
        administradores = Administrador.objects.all()
        for admin in administradores:
            usuarios.append({
                'email': admin.email,
                'contrasena': admin.contrasena,
                'rol': 'administrador'
            })

        # Obtener datos de Bodegueros
        bodegueros = Bodeguero.objects.all()
        for bodeguero in bodegueros:
            usuarios.append({
                'email': bodeguero.email,
                'contrasena': bodeguero.contrasena,
                'rol': 'bodeguero'
            })

        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)
    
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