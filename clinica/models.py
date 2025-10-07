from django.db import models

class Medico(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    foto = models.ImageField(upload_to='medicos/', blank=True, null=True)

    def __str__(self):
        return f'Dr(a). {self.nombre} {self.apellido}'
    
    # ... (Meta class opcional)
    
class Paciente(models.Model):
    # Clave foránea al modelo Medico
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE) 
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    historial = models.TextField()
    foto = models.ImageField(upload_to='pacientes/', blank=True, null=True)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'