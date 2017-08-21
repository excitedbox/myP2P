from django.forms import ModelForm
from .models import Lenders, Borrowers, Transaction, Registration
from django import forms


#creating forms from model (modelForm)
class PostFormLenders(ModelForm):
    class Meta:
        model = Lenders
        fields = ['lender_register_date', 'lender_outstanding_balance', 'lender_term_balance', 'transaction_key']
        widgets = {
           'lender_register_date': forms.Textarea(attrs={'cols': 80, 'rows': 20}), # attrs={'placeholder': 'Date of Registration', 'id': 'lenderRegistrationDate'}
           'lender_outstanding_balance': forms.TextInput(attrs={'placeholder': 'Loan Amount (in USD)', 'id': 'lenderOutstandingBalance'}),
           'lender_term_balance': forms.Textarea(attrs={'placeholder': 'Term balance (years)', 'id':'lenderTermBalance'}),
           'transaction_key': forms.HiddenInput()
        }

class PostFormBorrowers(ModelForm):
    class Meta:
        model = Borrowers
        fields = ['borrower_register_date','borrower_outstanding_balance','borrower_term_balance','transaction_key']
        widgets = {
            'borrower_register_date': forms.TextInput(attrs={'placeholder': 'Date of Registration', 'id': 'borrowerRegistrationDate'}),
            'borrower_outstanding_balance': forms.TextInput(attrs={'placeholder': 'Desired Loan Amount (in USD)', 'id': 'borrowerOutstandingBalance'}),
            'borrower_term_balance': forms.Textarea(attrs={'placeholder': 'Term balance (years)', 'id':'borrowerTermBalance'}),
            'transaction_key': forms.HiddenInput()
        }

class PostFormTransaction(ModelForm):
    class Meta:
        model = Transaction
        fields = ['transaction_date','transaction_borrower_interest_rate','transaction_lender_interest_rate','transaction_key']
        widgets = {
            'transaction_date': forms.TextInput(attrs={'id': 'transactionDate'}),
            'transaction_borrower_interest_rate': forms.TextInput(attrs={'id': 'transactionBorrowerRate'}),
            'transaction_lender_interest_rate': forms.Textarea(attrs={'id':'transactionLenderRate'}),
            'transaction_key': forms.Textarea(attrs={'id':'transactionKey'})
        }

class PostFormRegistration(ModelForm):
    class Meta:
        model = Registration
        fields = ['registration_date','user_first_name','user_last_name','user_email','username','password']
        widgets = {
            'registration_date': forms.TextInput(attrs={'id': 'registrationDate'}),
            'user_first_name': forms.TextInput(attrs={'id': 'firstName'}),
            'user_last_name': forms.TextInput(attrs={'id':'LastName'}),
            'user_email': forms.TextInput(attrs={'id': 'email'}),
            'username': forms.TextInput(attrs={'id':'userName'}),
            'password':forms.PasswordInput(attrs={'id':'password'})
        }

