from django.db import models

# Create your models here.
class Usuario(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    nombre = models.CharField(null=False, max_length=50)
    apellido = models.CharField(null=False, max_length=50)
    mail = models.EmailField(null=False, unique=True)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'