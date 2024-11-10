from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
import uuid

class Role(models.Model):
    role_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


# Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email,username, password=None, **extra_fields):
        """Create and return a regular user with an email and password."""
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email,username=username, **extra_fields)
        user.set_password(password)  # Hashes the password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        """Create and return a superuser with an email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(email, username,password, **extra_fields)


# Custom User model
class User(AbstractBaseUser):
    user_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.ForeignKey(Role, related_name="users", null=True, on_delete=models.PROTECT)
    password = models.CharField(max_length=128)  # Store the password hash
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)  # Can access the admin panel
    is_superuser = models.BooleanField(default=False)  # Is a superuser
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'  # Use email for authentication
    REQUIRED_FIELDS = ['first_name', 'last_name']  # Other fields to be required when creating a user

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def set_password(self, raw_password):
        """Override the default password setting to hash the password."""
        from django.contrib.auth.hashers import make_password
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """Override the default password check to validate hashed password."""
        from django.contrib.auth.hashers import check_password
        return check_password(raw_password, self.password)

    def has_perm(self, perm, obj=None):
        """Check if the user has a specific permission."""
        return self.is_superuser

    def has_module_perms(self, app_label):
        """Check if the user has permissions for a specific app."""
        return self.is_superuser

    @property
    def is_authenticated(self):
        """Always return True for an authenticated user."""
        return True

class Blog(models.Model):
    blogid = models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="blogs")
    title = models.CharField(max_length=200)
    content = models.TextField()