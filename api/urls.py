from django.urls import path, include
from rest_framework import routers
from api.views import AlumnoView, LoginView, CustomTokenObtainPairView

# Versioning
router = routers.DefaultRouter()
router.register(r'usuario', AlumnoView, 'Alumno')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
