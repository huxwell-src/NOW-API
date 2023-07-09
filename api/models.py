from django.db import models

class Carrera(models.Model):
    carrera_id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Curso(models.Model):
    curso_id = models.IntegerField(primary_key=True)
    grado = models.IntegerField()
    letra = models.CharField(max_length=2)

    def __str__(self):
        return f"Grado: {self.grado}, Letra: {self.letra}"


class EstadoSolicitud(models.Model):
    estado_id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Alumno(models.Model):
    rut = models.CharField(max_length=12, primary_key=True)
    nombre = models.CharField(max_length=50)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    email = models.CharField(max_length=255)
    contrasena = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Profesor(models.Model):
    rut = models.CharField(max_length=12, primary_key=True)
    nombre = models.CharField(max_length=50)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    email = models.CharField(max_length=255)
    contrasena = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Administrador(models.Model):
    rut = models.CharField(max_length=12, primary_key=True)
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    contrasena = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Bodeguero(models.Model):
    rut = models.CharField(max_length=12, primary_key=True)
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    contrasena = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Herramienta(models.Model):
    herramienta_id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    stock = models.IntegerField()
    medida_stock = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Solicitud(models.Model):
    solicitud_id = models.IntegerField(primary_key=True)
    alumno_rut = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    profesor_rut = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    fecha_solicitud = models.DateTimeField()
    fecha_entrega = models.DateTimeField()
    fecha_devolucion = models.DateTimeField()
    estado_id = models.ForeignKey(EstadoSolicitud, on_delete=models.CASCADE)

    def __str__(self):
        return f"Solicitud ID: {self.solicitud_id}"


class SolicitudAlumno(models.Model):
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    alumno_rut = models.ForeignKey(Alumno, on_delete=models.CASCADE)

    def __str__(self):
        return f"Solicitud ID: {self.solicitud.solicitud_id}, Alumno: {self.alumno_rut}"


class SolicitudHerramienta(models.Model):
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    herramienta = models.ForeignKey(Herramienta, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"Solicitud ID: {self.solicitud.solicitud_id}, Herramienta: {self.herramienta}"
