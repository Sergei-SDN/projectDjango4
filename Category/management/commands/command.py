from django.core.management.base import BaseCommand
from Category.models import Category


class Command(BaseCommand):
    help = 'Заполнить базу данных новыми данными'

    def handle(self, *args, **options):
        try:
            # Очищение базы данных от старых данных
            Category.objects.all().delete()

            # Заполнение базы данных новыми данными
            category_list = [
                {'name': 'New Category 1', 'description': 'New Description 1'},
                {'name': 'New Category 2', 'description': 'New Description 2'},
                {'name': 'New Category 3', 'description': 'New Description 3'},
                {'name': 'New Category 4', 'description': 'New Description 4'},
                {'name': 'New Category 5', 'description': 'New Description 5'},
                {'name': 'New Category 6', 'description': 'New Description 6'},
            ]

            # for category_item in category_list:
            # Category.objects.create(**category_item)

            # Category.objects.create(name='New Category 1', description='New Description 1')
            # Category.objects.create(name='New Category 2', description='New Description 2')

            category_create = []
            for category_item in category_list:
                category_create.append(
                    Category(**category_item)
                )

            Category.objects.bulk_create(category_create)

            self.stdout.write(self.style.SUCCESS('Data successfully added to the database'))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Failed to populate the database: {e}'))