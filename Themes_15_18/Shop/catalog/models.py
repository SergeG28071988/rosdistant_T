from django.db import models

# Create your models here.

from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = (
        ('Процессор', 'Процессор'),
        ('Материнская плата', 'Материнская плата'),
        ('Оперативная память', 'Оперативная память'),
        ('Видеокарта', 'Видеокарта'),
    )

    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)    
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)    

    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
