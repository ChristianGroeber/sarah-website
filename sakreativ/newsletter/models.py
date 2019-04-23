from django.db import models
from django.db.models import Model, CharField
import random


# Create your models here.


class Subscriber(Model):
    email_address = CharField(max_length=100, verbose_name='Email Adresse')
    unsubscribe_id = models.IntegerField(blank=True, null=True)
    subscribed = models.BooleanField(default=True)

    def __str__(self):
        return self.email_address

    def create_unsubscribe_id(self):
        rnd = random.randint(1, 10)
        self.unsubscribe_id = self.id * rnd
        self.save()
