from django.db import models

# Create your models here.
# erp/models.py
from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Employee(models.Model):
    ...

    class Meta:
        permissions = [
            ("can_add_employee", "Can add an employee"),
            ("can_view_employee", "Can view employees"),
        ]


from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
