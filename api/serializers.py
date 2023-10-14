from rest_framework import serializers
from .models import Alumno, Profesor, Administrador, Bodeguero, Solicitud, EstadoSolicitud, Herramienta

class EstadoSolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoSolicitud
        fields = '__all__'

class SolicitudSerializer(serializers.ModelSerializer):
    estado = EstadoSolicitudSerializer(source='estado_id', read_only=True)
    profesor_nombre = serializers.CharField(source='profesor_rut', read_only=True)
    alumno_nombre = serializers.CharField(source='alumno_rut', read_only=True)

    class Meta:
        model = Solicitud
        fields = '__all__'
        
class HerramientaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Herramienta 
        fields = '__all__'

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'

class ProfesorSerializer(serializers.ModelSerializer):
    rol = serializers.CharField(default='profesor')
    class Meta:
        model = Profesor
        fields = '__all__'

class AdministradorSerializer(serializers.ModelSerializer):
    rol = serializers.CharField(default='administrador')
    class Meta:
        model = Administrador
        fields = '__all__'

class BodegueroSerializer(serializers.ModelSerializer):
    rol = serializers.CharField(default='bodeguero')

    class Meta:
        model = Bodeguero
        fields = '__all__'
