from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    name_of_user = models.CharField(max_length=30, null=False)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    email = models.EmailField(_('email address'),unique=True)
    date_of_birth = models.DateTimeField(default=timezone.now)
    photo = models.ImageField(null=True, upload_to='users')

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    is_adoptant = models.BooleanField(default=False)
    is_rescuer = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Pet(models.Model):
    name = models.CharField(max_length=30, null=False)
    photo = models.ImageField(null=False, upload_to='pets')
    CATEGORY_CHOICES = [
    ('Perro', 'Perro'),
    ('Gato', 'Gato'),
    ('Otro', 'Otro'),
    ]
    category = models.CharField(max_length=10, null=False, choices=CATEGORY_CHOICES)
    specie = models.CharField(max_length=50)
    SEX_CHOICES = [
    ('Hembra', 'Hembra'),
    ('Macho', 'Macho'),
    ]
    sex = models.CharField(max_length=10, null=False, choices=SEX_CHOICES)
    SIZE_CHOICES = [
    ('Pequeña', 'Pequeña'),
    ('Mediana', 'Mediana'),
    ('Grande', 'Grande'),
    ]
    size = models.CharField(max_length=10, null=False, choices=SIZE_CHOICES)
    years = models.PositiveSmallIntegerField(null=True, blank=True)
    months = models.PositiveSmallIntegerField(null=True, blank=True)
    BOOLEAN_CHOICES = [
    ('Si', 'Si'),
    ('No', 'No'),
    ]
    is_kid_friendly = models.CharField(max_length=4, null=True, choices=BOOLEAN_CHOICES)
    is_dog_friendly = models.CharField(max_length=4, null=True, choices=BOOLEAN_CHOICES)
    is_cat_friendly = models.CharField(max_length=4, null=True, choices=BOOLEAN_CHOICES)
    vaccines = models.CharField(max_length=4, null=True, choices=BOOLEAN_CHOICES)
    sterilized = models.CharField(max_length=4, null=True, choices=BOOLEAN_CHOICES)
    PAYMENT_CHOICES = [
    ('Ninguno', 'Ninguno'),
    ('Económico', 'Económico'),
    ('Croquetas', 'Croquetas'),
    ]
    payment = models.CharField(max_length=10, null=False, choices=PAYMENT_CHOICES)
    STATUS_CHOICES = [
    ('Disponible', 'Disponible'),
    ('Pendiente', 'Pendiente'),
    ('Adoptado', 'Adoptado'),
    ]
    status = models.CharField(max_length=10, null=False, choices=STATUS_CHOICES)
    user_rescuer_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
        blank=True, related_name="rescuer_user")
    user_adoptant_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
        blank=True, related_name="adoptant_user")

class Questionary(models.Model):
    address_street = models.CharField(max_length=100, null=False)
    address_ext_num = models.PositiveSmallIntegerField(null=True, blank=True)
    address_int_num = models.CharField(max_length=6, null=True)
    address_city = models.CharField(max_length=80, null=False)
    address_zip_code = models.PositiveSmallIntegerField(null=False)
    BOOLEAN_CHOICES = [
    ('Y', 'Yes'),
    ('N', 'No'),
    ]
    pet_owner = models.CharField(max_length=4, null=False, choices=BOOLEAN_CHOICES)
    family_members = models.PositiveSmallIntegerField(null=False)
    family_agreement = models.CharField(max_length=4, null=False, choices=BOOLEAN_CHOICES)
    document_id = models.CharField(max_length=255, null=False)
    user_applicant_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applicant_user")
    user_autorizer_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="autorizer_user")
    STATUS_CHOICES = [
    ('APPROVED', 'Approved'),
    ('PENDING', 'Pending'),
    ('REJECTED', 'Rejected'),
    ]
    status = models.CharField(max_length=10, null=True, choices=STATUS_CHOICES)

class Request(models.Model):
    pet_id = models.ForeignKey(Pet, null=True, on_delete=models.SET_NULL, related_name="requested_pet")
    applicant_user_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="requester_user")
    approver_user_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="approver_user")
    STATUS_CHOICES = [
    ('OPEN', 'Open'),
    ('PENDING', 'Pending'),
    ('CLOSE', 'Close'),
    ]    
    status = models.CharField(max_length=10, null=True, choices=STATUS_CHOICES)
    