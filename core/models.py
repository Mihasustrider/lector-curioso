from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Usuario(AbstractUser):
    ROLES = (('gerente', 'Gerente'), ('empleado', 'Empleado'))
    rol = models.CharField(max_length=10, choices=ROLES, default='empleado')

    # Añadir estos dos campos para resolver el conflicto de nombres inversos
    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="usuario_set",  # Nombre único para la relación inversa
        related_query_name="usuario",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name="usuario_set",  # Nombre único para la relación inversa
        related_query_name="usuario",
    )

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Producto(models.Model):
    sku = models.CharField(max_length=50, unique=True, help_text="Stock Keeping Unit")
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20, blank=True, help_text="International Standard Book Number")
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    stock_actual = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.titulo