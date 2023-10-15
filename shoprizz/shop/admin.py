from django.contrib import admin
from . models import Customer, CustomerAddress, Address, Country

# Register your models here.
admin.site.register(Customer)
admin.site.register(CustomerAddress)
admin.site.register(Address)
admin.site.register(Country)