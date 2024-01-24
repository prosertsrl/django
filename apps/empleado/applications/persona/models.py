from django.db import models
# Importando la tabla Departamento
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

# Modelo Habilidades
class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)
    
    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'
        
    def __str__(self):
        return str(self.id) + '-' + self.habilidad

# Modelo Empleado
class Empleado(models.Model):
    #Modelo para la tabla empleado
    job_choices = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro'),
    )
    
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    job = models.CharField('Trabajo', max_length=1, choices=job_choices)
    # Relacion con la tabla departamento
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    #avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    # Relacion tabla Empleado y Habilidades
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()
    
    
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['first_name']
    
    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name