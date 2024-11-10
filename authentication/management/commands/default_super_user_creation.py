from django.core.management.base import BaseCommand
from authentication.models import Role, User


class Command(BaseCommand):
    help = 'Create a default superuser with predefined credentials'

    def handle(self, *args, **options):
        
        # Check if a superuser already exists
        if User.objects.filter(is_superuser=True).exists():
            self.stdout.write(self.style.SUCCESS("Superuser already exists. Skipping creation."))
            return

        # Predefined credentials (you can modify these)
        username = 'admin'
        email = 'admin@yourdomain.com'
        password = 'Admin1234!'  # Make sure this complies with your password policy

        # Create the user
        user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )

        # Assign the "Administrator" role
        admin_role = Role.objects.get(name="Administrator")
        user.role = admin_role
        user.save()

        self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' created with 'Administrator' role."))
