from django.db import models
from django.db.models import Model, CharField
import random


# Create your models here.


class Subscribers(Model):
    email_address = CharField(max_length=100, verbose_name='Email Adresse')
    unsubscribe_id = 0

    def __str__(self):
        return self.email_address

    def create_unsubscribe_id(self):
        self.unsubscribe_id = int(self.id) * random.random
