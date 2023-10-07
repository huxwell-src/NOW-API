from rest_framework import viewsets
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Alumno, Bodeguero, Profesor, Administrador, Solicitud, Herramienta, Carrera, Curso
from .serializers import AlumnoSerializer, BodegueroSerializer, ProfesorSerializer, AdministradorSerializer, SolicitudSerializer, HerramientaSerializer

class AlumnoView(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
    
    @action(detail=True, methods=['GET'])
    def solicitudes(self, request, pk=None):
        alumno = self.get_object()
        solicitudes = Solicitud.objects.filter(alumno_rut=alumno.rut)
        serializer = SolicitudSerializer(solicitudes, many=True)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = AlumnoSerializer(queryset, many=True)
        
        # Iterate through the results and replace carrera and curso IDs with their names
        for student in serializer.data:
            student['carrera'] = Carrera.objects.get(carrera_id=student['carrera']).nombre
            curso_id = student['curso']
            curso = Curso.objects.get(curso_id=curso_id)
            student['curso'] = f"{curso.grado}{curso.letra}"

        return Response(serializer.data)

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
    