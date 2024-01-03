from django.conf import settings
from django.db import models

from Category.models import Category
from users.models import NULLABLE


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    # name = models.CharField(max_length=100, verbose_name='Наименование', unique=True) unique проверяет уникольное значение
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='images/', null=True, verbose_name='Изображение (превью)')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за штуку')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='пользователь', on_delete=models.SET_NULL,
                              **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name='опубликовано')

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Наименование продукта')
    version_number = models.CharField(max_length=20, verbose_name='Номер версии')
    version_name = models.CharField(max_length=100, verbose_name='Наименование версии')
    is_current = models.BooleanField(default=False, verbose_name='Признак версии')

    def __str__(self):
        return f"{self.product.name} - {self.version_name} - {self.version_number}"

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
