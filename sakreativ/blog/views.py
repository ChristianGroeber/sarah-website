from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.


def index(request):
    posts = Post.objects.all()
    featured_post = None
    try:
        featured_post = Post.objects.get(featured=True)
    except Exception:
        print('there\'s no featured post')
    return render(request, 'blog/index.html', {'posts': posts, 'featured_post': featured_post})


def blog_post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/blog_post.html', {'post': post})
