

from django.db import models
from django.utils import timezone


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    # created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')  # новое поле

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'