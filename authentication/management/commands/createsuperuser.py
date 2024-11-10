import re
from django.contrib.auth.management.commands import createsuperuser
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import EmailValidator
from authentication.models import Role, User


class Command(createsuperuser.Command):
    help = "Create a superuser with a custom User model and role assignments."

    def handle(self, *args, **options):
        """
        Override to add role assignment for 'Administrator' and perform additional
        email and password validation.
        """
        self.role_admin = Role.objects.get(name="Administrator")

        super().handle(*args, **options)

        username = options['username']
        email = options['email']
        password = options['password']

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise ValidationError(_("User not found."))

        self.validate_email(email)

        self.validate_password(password)

        user.role.add(self.role_admin)
        user.save()

        self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' created with Administrator role."))

    def validate_email(self, email):
        """Advanced email validation"""
        try:
            EmailValidator()(email)
        except ValidationError:
            raise ValidationError(_("Enter a valid email address."))

        if not email.endswith('@yourdomain.com'):
            raise ValidationError(_("Email must be from the domain 'yourdomain.com'."))

    def validate_password(self, password):
        """Advanced password validation"""
        if len(password) < 8:
            raise ValidationError(_("Password must be at least 10 characters long."))
        
        if not re.search(r'[A-Z]', password):
            raise ValidationError(_("Password must contain at least one uppercase letter."))
        
        if not re.search(r'\d', password):
            raise ValidationError(_("Password must contain at least one number."))
        
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValidationError(_("Password must contain at least one special character."))