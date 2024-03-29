from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
from django.conf import settings
from django.template.loader import render_to_string


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    def get_initials(self):
        return 'NA'

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Wall(models.Model):
    """Wall model"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=100)
    body = models.TextField()

    def render(self):

        return render_to_string('nucleus/components/chart.html', {
            'series': '{"labels": ["1", "2", "3"], "datasets": [{"data": [1, 2, 3]}]}', # JSON object
            'height': 360,  # Optional 
        })

    def __str__(self):
        """A string representation of the Wall."""
        return self.title
