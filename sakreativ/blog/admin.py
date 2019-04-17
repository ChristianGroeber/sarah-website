from django.contrib import admin
from .models import Post, UeberMich, MyImage, Page, Gallery, Product, ShoppingCart
# Register your models here.


admin.site.register(Post)
admin.site.register(UeberMich)
admin.site.register(Page)
admin.site.register(MyImage)
admin.site.register(Gallery)
admin.site.register(Product)
admin.site.register(ShoppingCart)
