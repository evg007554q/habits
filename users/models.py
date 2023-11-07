# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')

class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='e-mail ')
    phone = models.CharField(max_length=35, verbose_name='Номер телефона', null=True, blank=True)
    city = models.CharField(max_length=10, verbose_name='город', null=True, blank=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', null=True, blank=True)
    key_user = models.CharField(max_length=12, verbose_name='Ключ', null=True, blank=True)
    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



# Create your models here.
