# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Lenders, Borrowers

# Register your models here.

admin.site.register(Lenders)
admin.site.register(Borrowers)
# admin.site.register(Transaction)
# admin.site.register(Transaction)
# admin.site.register(Registration)