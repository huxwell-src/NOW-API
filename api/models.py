from django.db import models

class EstadoSolicitud(models.Model):
    estado_id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Alumno(models.Model):
    rut = models.CharField(max_length=12, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50, default="")
    carrera = models.CharField(max_length=50)
    curso = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    contrasena = models.CharField(max_length=255, blank=True)  # Permite que el campo contrasena esté en blanco

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        # Generar contraseña automáticamente (primera letra del nombre en mayúscula + rut)
        if not self.contrasena:
            self.contrasena = self.apellido[0].upper() + self.rut
        super(Alumno, self).save(*args, **kwargs)


class Profesor(models.Model):
    rut = models.CharField(max_length=12, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50,  default="")
    carrera = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    contrasena = models.CharField(max_length=255, default="", blank=True)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        # Generar contraseña automáticamente (primera letra del nombre en mayúscula + rut)
        if not self.contrasena:
            self.contrasena = self.apellido[0].upper() + self.rut
        super(Profesor, self).save(*args, **kwargs)



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
    herramienta_id = models.AutoField(primary_key=True)  # Esto configurará el campo para incrementarse automáticamente
    nombre = models.CharField(max_length=50)
    stock = models.IntegerField()
    medida_stock = models.CharField(max_length=50)
    lvl_stock = models.CharField(max_length=10, blank=True, null=True)  # Campo para el nivel de stock

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        # Establecer el nivel de stock basado en el valor de stock
        if self.stock <= 10:
            self.lvl_stock = "bajo"
        elif 10 < self.stock <= 30:
            self.lvl_stock = "medio"
        else:
            self.lvl_stock = "adecuado"
        super(Herramienta, self).save(*args, **kwargs)




class Solicitud(models.Model):
    solicitud_id = models.IntegerField(primary_key=True)
    alumno_rut = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    profesor_rut = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    fecha_solicitud = models.DateField()
    fecha_entrega = models.DateField()
    fecha_devolucion = models.DateField()
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
