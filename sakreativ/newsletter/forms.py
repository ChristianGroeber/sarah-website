from django.forms import forms, models

from .models import Subscriber, Newsletter


class SubscriptionForm(models.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('email_address', )


class CreateNewsletter(models.ModelForm):
    class Meta:
        model = Newsletter
        exclude = ('sent', )
