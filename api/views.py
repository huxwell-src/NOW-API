from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Alumno, Profesor, Administrador, Bodeguero
from .serializers import AlumnoSerializer, ProfesorSerializer, AdministradorSerializer, BodegueroSerializer, LoginSerializer

class AlumnoView(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

class LoginView(APIView):
    def get(self, request):
        alumnos = Alumno.objects.all()
        profesores = Profesor.objects.all()
        administradores = Administrador.objects.all()
        bodegueros = Bodeguero.objects.all()

        serializer = LoginSerializer({
            'alumnos': alumnos,
            'profesores': profesores,
            'administradores': administradores,
            'bodegueros': bodegueros
        })

        return Response(serializer.data)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        refresh_token = response.data['refresh']
        access_token = response.data['access']

        response.data['refresh'] = refresh_token
        response.data['access'] = access_token
        return response
    