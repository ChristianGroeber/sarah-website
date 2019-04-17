from django.core.exceptions import ValidationError
from django.db import models
from froala_editor.fields import FroalaField
from PIL import Image

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
    only_show_to_me = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class MyImage(models.Model):
    image = models.ImageField(upload_to='gallery_picture')
    description = models.CharField(max_length=100, default='image')

    def __str__(self):
        return self.description

    def save(self, *args):
        super(MyImage, self).save(force_update=False)
        img = Image.open(self.image.path)
        img.thumbnail((300, 300), Image.ANTIALIAS)
        img.save(self.image.path)


class Gallery(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300, blank=True)
    images = models.ManyToManyField(MyImage)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    image = models.ImageField(upload_to='shop')

    def __str__(self):
        return self.title


class ShoppingCart(models.Model):
    items = models.ManyToManyField(Product)

    def __str__(self):
        return str(self.id)
