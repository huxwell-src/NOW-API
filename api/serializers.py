from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from .models import Alumno, Profesor, Administrador, Bodeguero

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ('email', 'contrasena')

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = ('email', 'contrasena')

class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = ('email', 'contrasena')

class BodegueroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bodeguero
        fields = ('email', 'contrasena')


class LoginSerializer(serializers.Serializer):
    alumnos = serializers.SerializerMethodField()
    profesores = serializers.SerializerMethodField()
    administradores = serializers.SerializerMethodField()
    bodegueros = serializers.SerializerMethodField()

    def get_alumnos(self, obj):
        alumnos = Alumno.objects.all()
        serializer = AlumnoSerializer(alumnos, many=True)
        tokens = self.get_tokens_for_user(alumnos)
        return {"data": serializer.data, "tokens": tokens}

    def get_profesores(self, obj):
        profesores = Profesor.objects.all()
        serializer = ProfesorSerializer(profesores, many=True)
        tokens = self.get_tokens_for_user(profesores)
        return {"data": serializer.data, "tokens": tokens}

    def get_administradores(self, obj):
        administradores = Administrador.objects.all()
        serializer = AdministradorSerializer(administradores, many=True)
        tokens = self.get_tokens_for_user(administradores)
        return {"data": serializer.data, "tokens": tokens}

    def get_bodegueros(self, obj):
        bodegueros = Bodeguero.objects.all()
        serializer = BodegueroSerializer(bodegueros, many=True)
        tokens = self.get_tokens_for_user(bodegueros)
        return {"data": serializer.data, "tokens": tokens}

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
