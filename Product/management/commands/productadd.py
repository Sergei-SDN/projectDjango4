import os

from django.conf import settings
from django.core.management.base import BaseCommand
from Category.models import Category
from Product.models import Product


class Command(BaseCommand):
    help = 'Populates the database with initial data'

    def handle(self, *args, **options):
        try:
            # Очищение базы данных от старых данных

            Product.objects.all().delete()
            Category.objects.all().delete()

            # Заполнение базы данных новыми данными
            category1 = Category.objects.create(name='New Category 1', description='New Description 1')
            category2 = Category.objects.create(name='New Category 2', description='New Description 2')

            product1 = Product.objects.create(name='New Product 1', description='New Description 1', category=category1,
                                              image='images/image.jpg', price=100)
            product2 = Product.objects.create(name='New Product 2', description='New Description 2', category=category2,
                                              image='images/image.jpg', price=200)

            self.stdout.write(self.style.SUCCESS('Data successfully added to the database'))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Failed to populate the database: {e}'))
