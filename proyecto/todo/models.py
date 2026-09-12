from django.db import models

class Tarea(models.Model):
    tarea = models.CharField(max_length=200)
    completada = models.BooleanField(default=False)
    fecha_limite = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.tarea