from django.db import models

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext as _
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=False,
        blank=True,
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[UnicodeUsernameValidator()],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        db_table = 'auth_user'

    def __str__(self):
        return self.email


class Location(models.Model):
    """Store information about the latitude, longtitude and place.
    """
    latitude = models.CharField(max_length=100)
    longtitude = models.CharField(max_length=100)
    place = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.place


class AddPresetLocation(Location):
    """Make proxy table for add preset location.
    """
    class Meta:
        proxy = True

    def __str__(self):
        return self.place

    class Meta:
        verbose_name = "Preset Location"
        verbose_name_plural = "Add Preset Loaction"


class UserFavouriteList(models.Model):
    """Store information about the user favourites photos.
    """
    title = models.CharField(max_length=500,blank=True)
    image_url = models.URLField(blank=True)
    latitude = models.CharField(max_length=500,blank=True)
    longtitude = models.CharField(max_length=500,blank=True)
    thumb_url = models.URLField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "User Favourite List"
        verbose_name_plural = "User Favourite List"
