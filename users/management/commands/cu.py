from django.core.management.base import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = 'Создание пользователя test'

    def handle(self, *args, **options):
        user = User.objects.create(
            email='test@sky.pro',
            first_name='test',
            last_name='test',
            is_staff=False,
            is_superuser=False,
            is_active=True,
        )

        user.set_password('123s')
        user.save()

