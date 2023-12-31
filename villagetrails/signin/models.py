from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.timezone import now
from .managers import VTUserManager

# Create your models here.
class VTUser(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='ID')
    phone = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=254)
    is_guest = models.BooleanField(default=True)
    otp = models.IntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)



    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = VTUserManager()

    def __str__(self):
        return str(self.phone)

