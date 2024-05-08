from django.db import models

# Create your models here.
class Tarea(models.Model):
    descripcion = models.CharField(max_length=100)
    estado= models.BooleanField(default=False)

    def __str__(self):
        return self.descripcion

class SubTarea(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.tarea}: {self.descripcion}"