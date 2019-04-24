from django.db import models
from django.db.models import Model, CharField, ForeignKey
from blog.models import Post
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


class Newsletter(Model):
    blog_post = ForeignKey(Post, on_delete=models.CASCADE)
    sent = models.BooleanField(default=False)

    def __str__(self):
        return str(self.blog_post)
