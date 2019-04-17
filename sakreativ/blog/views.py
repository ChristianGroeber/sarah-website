from django.shortcuts import render, get_object_or_404, redirect

from .forms import CustomerForm
from .models import Post, UeberMich, MyImage, Gallery, Product, ShoppingCart, AddedProduct
import smtplib
# Create your views here.


def index(request):
    posts = Post.objects.all().order_by('-date_posted')
    featured_post = Post.objects.filter(featured=True)
    return render(request, 'blog/index.html', {'posts': posts, 'featured_post': featured_post})


def blog_post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/blog_post.html', {'post': post, 'main_image': post.main_image})


def ueber_mich(request):
    return render(request, 'blog/about_me.html', {'ueber_mich': UeberMich.objects.get(pk=1)})


def gallery(request, gallery=None):
    if not gallery:
        return redirect('galerie/Galerie')
    list_images = Gallery.objects.get(title=gallery).images.all()
    num_images = len(list_images)/2 if len(list_images) % 2 == 0 else len(list_images)/2 + 1
    galleries = Gallery.objects.all()
    return render(request, 'blog/gallery.html', {'list_images': list_images, 'num_images': num_images, 'galleries': galleries})


def shop(request):
    products = Product.objects.all()
    price = 0
    if 'shopping_cart' in request.COOKIES:
        items = ShoppingCart.objects.get(pk=request.COOKIES['shopping_cart'])
        price = items.price()
    return render(request, 'blog/shop.html', {'products': products, 'price': price})


def add(request, product):
    response = redirect('shop')
    if 'shopping_cart' in request.COOKIES:
        cart = ShoppingCart.objects.get(pk=request.COOKIES['shopping_cart'])
    else:
        cart = ShoppingCart.objects.create()
        response.set_cookie('shopping_cart', value=cart.id)
    items = cart.items.all()
    print(items)
    product_to_add = Product.objects.get(pk=product)
    for item in items:
        print(str(item), product_to_add.title)
        if str(item) == str(product_to_add.title):
            item.amount += + 1
            item.save()
            break
    else:
        added_product = AddedProduct.objects.create(item=product_to_add)
        cart.items.add(added_product)
    return response


def checkout(request):
    shopping_cart = ShoppingCart.objects.get(pk=request.COOKIES['shopping_cart'])
    items = shopping_cart.items.all()
    print(items)
    return render(request, 'blog/shop_checkout.html', {'items': items, 'shopping_cart': shopping_cart})


def address(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            response = redirect('/')
            response.delete_cookie('shopping_cart')
            return response
    return render(request, 'blog/address.html', {'form': form})
