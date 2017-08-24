from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Lenders, Borrowers
from django import forms
from django.contrib.auth.models import User


#creating forms from model (modelForm)
class PostFormLenders(ModelForm):
    class Meta:
        model = Lenders
        fields = ['lender_outstanding_balance', 'lender_term_balance', 'lender_interest_rate']
        widgets = {
           'lender_outstanding_balance': forms.TextInput(attrs={'placeholder': 'Loan Amount (in USD)', 'id': 'lenderOutstandingBalance'}),
           'lender_term_balance': forms.TextInput(attrs={'placeholder': 'In years', 'id':'lenderTermBalance'}),
           'lender_interest_rate':forms.TextInput(attrs={'placeholder': 'in %', 'id': 'lenderRate'}),
        }

class PostFormBorrowers(ModelForm):
    class Meta:
        model = Borrowers
        fields = ['borrower_outstanding_balance','borrower_term_balance','borrower_interest_rate']
        widgets = {
            'borrower_outstanding_balance': forms.TextInput(attrs={'placeholder': 'Desired Loan (in USD)', 'id': 'borrowerOutstandingBalance'}),
            'borrower_term_balance': forms.TextInput(attrs={'placeholder': 'In years', 'id':'borrowerTermBalance'}),
            'borrower_interest_rate': forms.TextInput(attrs={'placeholder': 'in %', 'id': 'borrowerRate'}),
        }

# class PostFormTransaction(ModelForm):
#     class Meta:
#         model = Transaction
#         fields = ['transaction_date','transaction_borrower_interest_rate','transaction_lender_interest_rate','transaction_key']
#         widgets = {
#             'transaction_date': forms.TextInput(attrs={'id': 'transactionDate'}),
#             'transaction_borrower_interest_rate': forms.TextInput(attrs={'id': 'transactionBorrowerRate'}),
#             'transaction_lender_interest_rate': forms.Textarea(attrs={'id':'transactionLenderRate'}),
#             'transaction_key': forms.Textarea(attrs={'id':'transactionKey'})
#         }

class PostFormRegistration(UserCreationForm):
    user_first_name = forms.TextInput(attrs={'id': 'firstName'})
    user_last_name = forms.TextInput(attrs={'id':'LastName'})
    user_email = forms.TextInput(attrs={'id': 'email'})

    class Meta:
        model = User
        # fields = '__all__'
        fields = ('username','first_name','last_name','email')
        # fields = ('username', 'user_first_name', 'user_last_name', 'user_email',)
        #widgets = {
        #     'registration_date': forms.TextInput(attrs={'id': 'registrationDate'}),
        #     'user_first_name': forms.TextInput(attrs={'id': 'firstName'}),
        #     'user_last_name': forms.TextInput(attrs={'id':'LastName'}),
        #     'user_email': forms.TextInput(attrs={'id': 'email'}),
        #     'username': forms.TextInput(attrs={'id':'userName'}),
        #     'password':forms.PasswordInput(attrs={'id':'password'})
        #}

