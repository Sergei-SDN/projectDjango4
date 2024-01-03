from django.db import models

# Create your models here.

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=200, verbose_name='Slag', **NULLABLE)
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='images/', **NULLABLE,
                                verbose_name='Превью (изображение)')  # Место, куда сохраняются изображения
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    published = models.BooleanField(default=False, verbose_name='Признак публикации')
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'  # Установка человекочитаемого имени модели
        verbose_name_plural = 'Blogs'  # Установка человекочитаемого имени модели во множественном числе
