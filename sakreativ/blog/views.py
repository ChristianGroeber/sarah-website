from django.shortcuts import render, get_object_or_404
from .models import Post, UeberMich
# Create your views here.


def index(request):
    posts = Post.objects.all()
    featured_post = Post.objects.filter(featured=True)
    return render(request, 'blog/index.html', {'posts': posts, 'featured_post': featured_post})


def blog_post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/blog_post.html', {'post': post})


def ueber_mich(request):
    return render(request, 'blog/about_me.html', {'ueber_mich': UeberMich.objects.get(pk=1)})
