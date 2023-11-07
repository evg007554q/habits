from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='Admin@test.test',
            first_name='Admin',
            last_name='Admin',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )

        user.set_password('1')
        user.save()

        usertest = User.objects.create(
            email='test@test.test',
            first_name='test',
            last_name='test',
            is_superuser=False,
            is_staff=False,
            is_active=True
        )

        usertest.set_password('1')
        usertest.save()ccsu.py