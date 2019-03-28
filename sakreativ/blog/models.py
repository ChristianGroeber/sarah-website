from django.core.exceptions import ValidationError
from django.db import models
from froala_editor.fields import FroalaField

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=300, default='Lies meinen neuesten Beitrag')
    date_posted = models.DateTimeField()
    text = FroalaField()
    main_image = models.ImageField(blank=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class UeberMich(models.Model):
    title = models.CharField(blank=False, max_length=500, default='')
    text = FroalaField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if UeberMich.objects.exists() and not self.pk:
            raise ValidationError('There is can be only one JuicerBaseSettings instance')
        return super(UeberMich, self).save(*args, **kwargs)


class Page(models.Model):
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=200)
    show_on_page = models.BooleanField(default=True)

    def __str__(self):
        return self.title
