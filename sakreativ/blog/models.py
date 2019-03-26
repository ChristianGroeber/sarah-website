from django.db import models

# Create your models here.
from tinymce import HTMLField


class Post(models.Model):
    date_posted = models.DateTimeField()
    title = models.CharField(max_length=255)
    text = HTMLField('Content')
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class PostList(models.Model):
    posts = models.ManyToManyField(Post, limit_choices_to=20)
