# Generated by Django 4.2.7 on 2023-12-30 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(null=True, upload_to='images/', verbose_name='Изображение (превью)')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена за штуку')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')),
                ('is_published', models.BooleanField(default=False, verbose_name='опубликовано')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Category.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.CharField(max_length=20, verbose_name='Номер версии')),
                ('version_name', models.CharField(max_length=100, verbose_name='Наименование версии')),
                ('is_current', models.BooleanField(default=False, verbose_name='Признак версии')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.product', verbose_name='Наименование продукта')),
            ],
            options={
                'verbose_name': 'Версия',
                'verbose_name_plural': 'Версии',
            },
        ),
    ]
