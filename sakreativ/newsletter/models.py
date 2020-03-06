from django.db import models
from django.db.models import Model, CharField, ForeignKey
from blog.models import Post
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.utils import timezone
import hashlib


# Create your models here.


class Subscriber(Model):
    email_address = CharField(max_length=100, verbose_name='Email Adresse')
    unsubscribe_id = models.CharField(max_length=255, blank=True, null=True)
    subscribed = models.BooleanField(default=True)
    date_subscribed = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.email_address

    def create_unsubscribe_id(self):
        self_dict = {'id': self.id, 'email': self.email_address, 'date_subscribed': self.date_subscribed.strftime('%Y-%m-%d_%H-%M')}
        self.unsubscribe_id = hashlib.sha256(json.dumps(self_dict).encode('utf-8')).hexdigest()

    class Meta:
        verbose_name = 'Abonnent'
        verbose_name_plural = 'Abonnenten'


class Newsletter(Model):
    blog_post = ForeignKey(Post, on_delete=models.CASCADE)
    sent = models.BooleanField(default=False)

    def __str__(self):
        return str(self.blog_post)
