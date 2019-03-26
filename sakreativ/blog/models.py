from django.db import models

# Create your models here.
from tinymce import HTMLField


class Post(models.Model):
    date_posted = models.DateTimeField()
    title = models.CharField(max_length=255)
    text = HTMLField('Content')
