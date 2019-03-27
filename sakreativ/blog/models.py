from django.db import models
from froala_editor.fields import FroalaField

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    date_posted = models.DateTimeField()
    text = FroalaField()
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class PostList(models.Model):
    posts = models.ManyToManyField(Post, limit_choices_to=20)
