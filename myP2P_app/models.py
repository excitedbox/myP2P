# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Lenders(models.Model):
    lender_register_date = models.ForeignKey('Registration', on_delete=models.CASCADE)
    lender_outstanding_balance = models.DecimalField(max_digits=10, decimal_places=2)
    lender_term_balance = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_key = models.ForeignKey('Transaction', on_delete=models.CASCADE)

class Borrowers(models.Model):
    borrower_register_date = models.ForeignKey('Registration', on_delete=models.CASCADE)
    borrower_outstanding_balance = models.DecimalField(max_digits=10, decimal_places=2)
    borrower_term_balance = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_key = models.ForeignKey('Transaction', on_delete=models.CASCADE)

class Transaction(models.Model):
    transaction_date = models.DateTimeField('date posted')
    transaction_borrower_interest_rate = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_lender_interest_rate = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_balance = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_key = models.AutoField(primary_key = True)

class Registration(models.Model):
    registration_date = models.AutoField(primary_key=True)
    user_first_name = models.CharField("First Name", max_length=30)
    user_last_name = models.CharField("Last name", max_length=30)
    user_email = models.CharField("Email address", max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)



