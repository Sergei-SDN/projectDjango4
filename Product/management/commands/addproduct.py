from django.core.management.base import BaseCommand
import os
from django.conf import settings
from Product.models import Product


class Command(BaseCommand):
    help = 'Заполнить базу данных новыми данными'

    def handle(self, *args, **options):
        # Очищение базы данных от старых данных
        Product.objects.all().delete()

        # Заполнение базы данных новыми данными
        product_list = [
            {
                'name': 'New Product 1',
                'description': 'New Description 1',
                'image': 'images/image.jpg',
                'category': '1',
                'price': '100$'
            },
            {
                'name': 'New Product 2',
                'description': 'New Description 2',
                'image': 'images/image.jpg',
                'category': '2',
                'price': '200$',
            },

        ]

        product_create = []
        for product_item in product_list:
            product_create.append(
                Product(**product_item)
            )

        Product.objects.bulk_create(product_create)

        print('Данные успешно добавлены в базу данных')

        # for category_item in category_list:
        # Category.objects.create(**category_item)

        # Category.objects.create(name='New Category 1', description='New Description 1')
        # Category.objects.create(name='New Category 2', description='New Description 2')
