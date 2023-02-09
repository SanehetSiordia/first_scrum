from django.db import models
from datetime import date

# Create your models here.
class usuario(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50,verbose_name='Nombre',null=False)
    primer_apellido=models.CharField(max_length=50,verbose_name='Primer Apellido',null=False)
    segundo_apellido=models.CharField(max_length=50,verbose_name='Segundo Apellido',null=False)
    fecha=models.DateField(verbose_name='Fecha de Nacimiento',null=False)
    ciudad=models.CharField(max_length=50,verbose_name='ciudad',null=False)
    estado=models.CharField(max_length=50,verbose_name='estado',null=False)
    numero=models.BigIntegerField(verbose_name='Telefono',null=True)

    
    def __str__(self):
        fila=f'Nombre: {self.nombre} {self.primer_apellido} {self.segundo_apellido} | Cumpleaños: {self.fecha}'  
        return fila

    def delete(self, using:None, keep_parents: False):
        return super().delete()
    
    @property
    def apellido(self):
        return f'{self.primer_apellido} {self.segundo_apellido}'
    
    @property
    def edad(self):
        days_in_year = 365.2425   
        age = int((date.today() - self.fecha).days / days_in_year)        
        return age
    