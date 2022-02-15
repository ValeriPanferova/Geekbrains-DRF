from django.core.management.base import BaseCommand, CommandError

from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):

    def handle(self, *args, **options):

        try:
            User.objects.create_user(username='admin',
                                     email='superuser@super.com',
                                     password='admin',
                                     is_staff=True,
                                     is_active=True,
                                     is_superuser=True
                                     )
        except:
            pass
