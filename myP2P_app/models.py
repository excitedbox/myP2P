# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Lenders(models.Model):
    lender_outstanding_balance = models.DecimalField(max_digits=10, decimal_places=2)
    lender_term_balance = models.DecimalField(max_digits=10, decimal_places=2)
    # lender_transaction_key = models.AutoField(primary_key=True)
    lender_interest_rate = models.DecimalField(max_digits=10, decimal_places=2)
    lender_user_id = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.lender_user_id)

class Borrowers(models.Model):
    borrower_outstanding_balance = models.DecimalField(max_digits=10, decimal_places=2)
    borrower_term_balance = models.DecimalField(max_digits=10, decimal_places=2)
    # borrower_transaction_key = models.AutoField(primary_key=True)
    borrower_interest_rate = models.DecimalField(max_digits=10, decimal_places=2)
    borrower_user_id = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.borrower_user_id)

# class Transaction(models.Model):
#     transaction_date = models.DateTimeField('date posted')
#     transaction_borrower_interest_rate = models.DecimalField(max_digits=10, decimal_places=2)
#     transaction_lender_interest_rate = models.DecimalField(max_digits=10, decimal_places=2)
#     transaction_balance = models.DecimalField(max_digits=10, decimal_places=2)
#     transaction_key = models.AutoField(primary_key = True)




# class Registration(models.Model):
#     registration_date = models.AutoField(primary_key=True)
#     user_first_name = models.CharField("First Name", max_length=30)
#     user_last_name = models.CharField("Last name", max_length=30)
#     user_email = models.CharField("Email address", max_length=100)
#     username = models.OneToOneField(User,on_delete=models.CASCADE)
#     password = models.CharField(max_length=100)




