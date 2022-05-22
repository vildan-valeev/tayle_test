from django import forms
from django.forms import ModelForm, TextInput, EmailInput, NumberInput, SelectMultiple, Select, Textarea

from .models import AccountBillTransaction

class TransactionForm(ModelForm):
    class Meta:
        model = AccountBillTransaction
        fields = ['from_bills', 'to_bill', 'comment', 'amount']
        widgets = {
            'from_bills': SelectMultiple(attrs={
                'class': "form-select",
                'aria-label': "multiple select example",
            }),
            'to_bill': Select(attrs={
                'class': "form-select",
                'aria - label': "Default select example",
            }),
            'comment': Textarea(attrs={
                'class': "form-control",
                'aria - label': "Default select example",
                'style': 'height: 100px'
            }),
            'amount': NumberInput(attrs={
                'class': "form-control",
                'placeholder': '999'
                }),

        }
