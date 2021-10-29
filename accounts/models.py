from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self, email,name,is_counselor = False, password=None, **other_fields):
        """
        Creates and saves a User with the given email and password.
        """

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name = name,
            is_counselor = is_counselor,
            **other_fields
        )

        user.set_password(password)
        user.save()
        return user



    def create_superuser(self, email,name,is_counselor = False, password=None, **other_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        other_fields.setdefault('is_active',True)
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        if other_fields.get('is_active') is not True: 
            raise ValueError('error1')
        if other_fields.get('is_staff') is not True:
            raise ValueError('error2')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('error3')
        return self.create_user(email,name = name,password=password,**other_fields)

class Account(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(verbose_name = 'email address',max_length=255,unique=True)
    name = models.CharField(max_length=255, verbose_name='username')
    is_active = models.BooleanField(default=True)
    is_counselor = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name

class BioPsikolog(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    bio = models.TextField()

    def __str__(self):
        return self.user.username
