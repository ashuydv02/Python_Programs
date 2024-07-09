from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, unique=True)
    address = models.CharField(max_length=100)
    department = models.CharField(max_length=20)
    phone_no = models.IntegerField()

    def __str__(self):
        return self.name
