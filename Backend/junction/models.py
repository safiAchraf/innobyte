from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class user(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=30)
    staff = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=20 , null=True)
    # Add your custom fields for instructors here

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'phone_number']

    def __str__(self):
        return self.email

class room(models.Model):
    capacity = models.IntegerField()
    price = models.IntegerField()
    summary = models.CharField(max_length=100)
    room_number = models.IntegerField()
    sea_view = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    available_at = models.DateField()
    suite = models.BooleanField(default=False)




class reservation(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.IntegerField()
    room_id = models.ForeignKey(room, on_delete=models.CASCADE)  

class review(models.Model):
    reservation_id = models.ForeignKey(reservation, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.CharField(max_length=100)


class tasks(models.Model):
    title = models.CharField(max_length=30)
    desctiprion = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

