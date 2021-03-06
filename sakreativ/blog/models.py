from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import ForeignKey
from froala_editor.fields import FroalaField
from PIL import Image

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=300, default='Lies meinen neuesten Beitrag', verbose_name='Beschreibung')
    date_posted = models.DateTimeField(verbose_name='Datum geposted')
    text = FroalaField()
    main_image = models.ImageField(blank=True, verbose_name='Hauptbild')
    featured = models.BooleanField(default=False, verbose_name='Hervorgehoben')

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

    class Meta:
        verbose_name = 'Über mich'
        verbose_name_plural = 'Über mich '


class Page(models.Model):
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=200)
    show_on_page = models.BooleanField(default=True, verbose_name='Auf der Seite anzeigen')
    only_show_to_me = models.BooleanField(default=False, verbose_name='Nur dem Admin zeigen')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Seite'
        verbose_name_plural = 'Seiten'


class MyImage(models.Model):
    image = models.ImageField(upload_to='gallery_picture', verbose_name='Bild')
    description = models.CharField(max_length=100, default='image', verbose_name='Beschreibung')

    def __str__(self):
        return self.description

    def save(self, *args):
        super(MyImage, self).save(force_update=False)
        img = Image.open(self.image.path)
        img.thumbnail((300, 300), Image.ANTIALIAS)
        img.save(self.image.path)

    class Meta:
        verbose_name = 'Bild'
        verbose_name_plural = 'Bilder'


class Gallery(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300, blank=True, verbose_name='Beschreibung')
    images = models.ManyToManyField(MyImage, verbose_name='Bilder')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Galerie'
        verbose_name_plural = 'Galerien'


class ClothingSize(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Kleider Grösse'
        verbose_name_plural = 'Kleider Grössen'


class ShopCategory(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500, blank=True, verbose_name='Beschreibung')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Shop Kategorie'
        verbose_name_plural = 'Shop Kategorien'


class Product(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500, verbose_name='Beschreibung', blank=True)
    price = models.IntegerField(verbose_name='Preis')
    image = models.ImageField(upload_to='shop', verbose_name='Bild')
    category = ForeignKey(ShopCategory, on_delete=models.CASCADE, verbose_name='Kategorie')
    size = models.ManyToManyField(ClothingSize, blank=True, verbose_name='Grösse')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Produkt'
        verbose_name_plural = 'Produkte'


class AddedProduct(models.Model):
    item = ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

    def __str__(self):
        return str(self.item.title)

    def price(self):
        return int(self.item.price) * int(self.amount)

    class Meta:
        verbose_name = 'Hinzugefügtes Produkt'
        verbose_name_plural = 'Hinzugefügte Produkte'


class ShoppingCart(models.Model):
    items = models.ManyToManyField(AddedProduct)

    def __str__(self):
        return str(self.id)

    def price(self):
        price = 0
        for item in self.items.all():
            price += item.price()
        return price

    class Meta:
        verbose_name = 'Einkaufswagen'
        verbose_name_plural = 'Einkaufswagen'


class Customer(models.Model):
    name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50, name='Vorname')
    address = models.CharField(max_length=200, name='Adresse')
    town = models.CharField(max_length=50, name='Wohnort')
    zip_code = models.IntegerField(name='PLZ')
    country = models.CharField(max_length=50, default='Schweiz', name='Land')
    email_address = models.EmailField()

    def __str__(self):
        return str(self.first_name) + " " + str(self.name)

    class Meta:
        verbose_name = 'Kunde'
        verbose_name_plural = 'Kunden'