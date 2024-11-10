from django.core.management.base import BaseCommand
from authentication.models import Role


class Command(BaseCommand):
    help = 'Create predefined roles for the system'

    def handle(self, *args, **options):
        roles = ["Administrator", "HR", "Manager", "Developer", "EndUser"]

        for role_name in roles:
            role,created = Role.objects.get_or_create(name=role_name, description=None)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Role '{role_name}' created."))
            else:
                self.stdout.write(self.style.SUCCESS(f"Role '{role_name}' already exists."))
