from django.db import models


# Create your models here.
class Sexo(models.Model):
    """docstring for Sexo"""
    def __init__(self, *args, **kwargs):
        super(Sexo, self).__init__(*args, **kwargs)
    sexo = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.sexo

    class Meta:
        verbose_name = "Sexo"
        verbose_name_plural = "Sexos"
        ordering = ['sexo']


class Estado_civil(models.Model):
    """docstring for Estado_civil"""
    def __init__(self, *args, **kwargs):
        super(Estado_civil, self).__init__(*args, **kwargs)
    estado_civil = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.estado_civil

    class Meta:
        verbose_name = "Estado civil"
        verbose_name_plural = "Estados civil"
        ordering = ['estado_civil']


class Cliente(models.Model):
    """docstring for Cliente"""
    def __init__(self, *args, **kwargs):
        super(Cliente, self).__init__(*args, **kwargs)

    nombre_principal = models.CharField(max_length=250)
    dni = models.CharField(max_length=15)
    sexo = models.ForeignKey(Sexo)
    estado_civil = models.ForeignKey(Estado_civil)
    fecha_nacimiento = models.DateTimeField(blank=True)
    comentarios = models.TextField(blank=True)
    adicional1 = models.CharField(max_length=50, blank=True)
    adicional2 = models.CharField(max_length=50, blank=True)
    adicional3 = models.CharField(max_length=50, blank=True)
    adicional4 = models.CharField(max_length=50, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_principal

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['nombre_principal']


class Email(models.Model):

    email = models.EmailField(unique=True)
    cliente = models.ForeignKey(Cliente, default=1)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Email"
        verbose_name_plural = "Emails"
        ordering = ['cliente', 'email']
