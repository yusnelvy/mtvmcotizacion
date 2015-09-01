from django.db import models


# Create your models here.
class Cargo_trabajador(models.Model):
    """docstring for Cargo_trabajador"""
    def __init__(self, *args, **kwargs):
        super(Cargo_trabajador, self).__init__(*args, **kwargs)

    cargo = models.CharField(max_length=100, unique=True)
    tarifa_dia = models.DecimalField(max_digits=9, decimal_places=2)
    recargo_fin_semana = models.DecimalField(max_digits=9, decimal_places=2)
    recargo_nocturno = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.cargo

    class Meta:
        verbose_name = "Cargo de trabajador"
        verbose_name_plural = "Cargos de trabajadores"
        ordering = ['cargo']
