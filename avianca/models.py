from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Vuelo(models.Model):

    TIPOS_VUELO = [
        ('Nacional', 'Nacional'),
        ('Nacional', 'Internacional'),
    ]

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255, choices=TIPOS_VUELO)
    precio = models.IntegerField(validators=[MinValueValidator(50), MaxValueValidator(5000)], default=1)
