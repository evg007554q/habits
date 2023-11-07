from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):


        usertest = User.objects.create(
            email='test@test.test',
            first_name='test',
            last_name='test',
            is_superuser=False,
            is_staff=False,
            is_active=True
        )

        usertest.set_password('1')
        usertest.save()