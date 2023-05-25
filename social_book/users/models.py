from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    full_name = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=10, null=True)
    city = models.CharField(max_length=25, default="Pune")
    state = models.CharField(max_length=25, default="Maharashtra")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    public_visibility = models.BooleanField(default=False)
    age = models.IntegerField(default=0)
    birth_year = models.IntegerField(default=0)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [full_name, gender, city, state, public_visibility, age, birth_year]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    

class UploadBooks(models.Model):
    CustomUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False)
    description = models.TextField(max_length=500, null=False)
    visibility = models.BooleanField(default=True, null=False)
    cost = models.IntegerField(null=False)
    year_of_publishing = models.IntegerField(null=False)
    cover_image = models.ImageField(null=False, upload_to='book_cover/')
    book_path = models.FileField(null=False, upload_to='book/')

class UploadImage(models.Model):
    CustomUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_picture', null=True)
