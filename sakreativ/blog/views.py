from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, UeberMich, MyImage, Gallery
# Create your views here.


def index(request):
    posts = Post.objects.all()
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
