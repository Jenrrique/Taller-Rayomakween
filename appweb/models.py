from django.db import models

# Create your models here.
class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Profesional(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField(null=True, blank=True)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to="profesional", null=True, blank=True)

    def __str__(self):
        return self.rut

tipo_contacto = [
    [0, "Sugerencia"],
    [1, "Reclamo"],
    [2, "Felicitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    telefono = models.IntegerField()
    tipo_contacto = models.IntegerField(choices=tipo_contacto)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre + " " + self.email
    
class Postular(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rut = models.CharField(max_length=10, null=True)
    titulo = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    telefono = models.IntegerField()
    descripcion = models.TextField()
    experiencia = models.TextField()
    foto = models.ImageField(upload_to="postular", null=True)

    def __str__(self):
        return self.nombre + " " + self.email    

estado = [
    [0, "Pendiente"],
    [1, "Aceptado"],
    [2, "Rechazado"],
    [3, "Completado"]
]

categoria = [
    [0, "Cambio de neumáticos"],
    [1, "Cambio de aceite"],
    [2, "Abolladura"],
    [3, "Revisión de batería"],
    [4, "Cambio de batería"],
    [5, "Revisión de niveles"],
    [6, "Caja de cambio"],
    [7, "Cambio de pastillas de freno"],
    [8, "Limpieza"]
]    

class Solicitud(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.IntegerField(choices=categoria)
    email = models.CharField(max_length=100)
    telefono = models.IntegerField()
    fecha = models.DateField(null=True)
    foto = models.ImageField(upload_to="solicitud", null=True)
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE, null=True)
    estado = models.IntegerField(choices=estado, null=True)
    descripcion = models.TextField(null=True) 
    
    def __str__(self):
        return self.email
    
class Trabajo(models.Model):
    nombre = models.CharField(max_length=100)
    costo = models.CharField(max_length=100)
    categoria = models.IntegerField(choices=categoria)
    foto = models.ImageField(upload_to="trabajo", null=True)
    descripcion = models.TextField() 

    def __str__(self):
        return self.nombre 



