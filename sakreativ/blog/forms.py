from django.forms import forms, models

from .models import Customer


class CustomerForm(models.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'Vorname', 'Adresse', 'Wohnort', 'PLZ', 'Land', 'email_address')
