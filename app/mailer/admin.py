#-*- coding: utf-8 -*-
from django.contrib import admin
from .models import Company, Order, Contact

admin.site.register(Company)
admin.site.register(Order)
admin.site.register(Contact)
