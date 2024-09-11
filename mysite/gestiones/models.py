from django.db import models

# Create your models here.

class Gestiones (models.Model):
    gestion_id = models.AutoField(primary_key=True)
    nombre_gestion = models.CharField(null=False, max_length=50)
    descripcion = models.CharField(null=False, max_length=50)
    

    
    