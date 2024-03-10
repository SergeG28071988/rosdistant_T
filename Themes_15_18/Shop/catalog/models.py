from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Производитель", blank=False)
    country = models.CharField(max_length=100, verbose_name="Страна", blank=False)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    CATEGORY_CHOICES = (
        ('Процессор', 'Процессор'),
        ('Материнская плата', 'Материнская плата'),
        ('Оперативная память', 'Оперативная память'),
        ('Видеокарта', 'Видеокарта'),
    )

    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE, 
                                     verbose_name="Производитель")
    name = models.CharField(max_length=255, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    quantity = models.PositiveIntegerField(verbose_name="Количество")
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Цена")    
    category = models.CharField(max_length=20, verbose_name="Категория", choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='media/images/', verbose_name="Фото товара")

    def __str__(self):
        return self.name