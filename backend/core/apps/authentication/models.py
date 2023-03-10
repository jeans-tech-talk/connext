from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone
from encrypted_fields.fields import EncryptedCharField

from core.apps.authentication.choices import Sex, EducationLevel, Occupation


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
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=6, choices=Sex.choices)
    birthday = models.DateField()
    id_card_number = EncryptedCharField(max_length=17, unique=True)
    id_card_image = models.ImageField(upload_to='id-card-images/%Y-%m-%d/')
    image = models.ImageField(upload_to='user-images/%Y-%m-%d/')
    address = models.TextField()
    phone_number = models.CharField(max_length=12, unique=True)
    education_level = models.CharField(max_length=18, choices=EducationLevel.choices)
    occupation = models.CharField(max_length=29, choices=Occupation.choices)
    bank_account = models.OneToOneField(
        'finance.BankAccount',
        on_delete=models.SET_NULL,
        related_name='user',
        null=True,
        blank=True,
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        db_table = 'authentication_user'


User = get_user_model()
