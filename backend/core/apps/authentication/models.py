from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone

from core.apps.authentication.choices import Sex, EducationLevel, Occupation


class BankAccount(models.Model):
    bank = models.CharField(max_length=150)
    branch = models.CharField(max_length=150)
    account_name = models.CharField(max_length=150)
    account_number = models.CharField(max_length=150)

    objects = models.Manager()

    class Meta:
        db_table = 'authentication_bank_account'


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The email must be set')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=6, choices=Sex.choices, blank=True)
    birthday = models.DateField(null=True)
    id_card_number = models.CharField(max_length=17, blank=True)
    id_card_image = models.ImageField(upload_to='id-card-images/%Y-%m-%d/', blank=True)
    image = models.ImageField(upload_to='user-images/%Y-%m-%d/', blank=True)
    address = models.TextField(blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    education_level = models.CharField(max_length=18, choices=EducationLevel.choices, blank=True)
    occupation = models.CharField(max_length=29, choices=Occupation.choices, blank=True)
    bank_account = models.OneToOneField(
        'authentication.BankAccount',
        on_delete=models.SET_NULL,
        related_name='user',
        null=True,
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        db_table = 'authentication_custom_user'


User = get_user_model()
