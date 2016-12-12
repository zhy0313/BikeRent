from django.contrib import admin

from Bike.models import *
# Register your models here.

admin.site.register(Person)
admin.site.register(Bike)
admin.site.register(Order)