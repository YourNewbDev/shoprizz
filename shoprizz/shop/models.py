from django.db import models, IntegrityError
from django.core.validators import MaxValueValidator
from django.contrib.auth.hashers import make_password
import random, string

# Create your models here.
class Customer(models.Model):
    customer_first_name = models.CharField(max_length=155)
    customer_last_name = models.CharField(max_length=100)
    customer_phone_number = models.IntegerField(validators=[MaxValueValidator(99999999999)])
    customer_username = models.CharField(max_length=10, unique=True)
    customer_email = models.EmailField(max_length=255, unique=True)
    customer_password = models.CharField(max_length=12)
    customer_registered_date = models.DateField(auto_now_add=True)

    # Hash password
    def hash_pass(self, *args, **kwargs):
        self.customer_password = make_password(self.customer_password)
        super(Customer, self).save(*args, **kwargs)

class Country(models.Model): # null temporarily while looking for python package
    country_name = models.CharField(max_length=90, null=True, blank=True)

class Address(models.Model): # null temporarily while looking for python package
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    address_region = models.CharField(max_length=155, null=True, blank=True)
    address_province = models.CharField(max_length=155, null=True, blank=True)
    address_city = models.CharField(max_length=155, null=True, blank=True)
    address_postal = models.CharField(max_length=5, null=True, blank=True)
    address_unit = models.CharField(max_length=10, null=True, blank=True)
    address_street = models.CharField(max_length=50, null=True, blank=True)
    address_line1 = models.CharField(max_length=255, null=True, blank=True)
    address_line2 = models.CharField(max_length=255, null=True, blank=True)

class CustomerAddress(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    is_default = models.BooleanField(default=False)