from django.forms import forms, models

from .models import Subscriber


class SubscriptionForm(models.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('email_address', )
