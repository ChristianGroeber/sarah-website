from django.shortcuts import render, redirect
from .models import Subscriber

# Create your views here.


def index(request):
    if str(request.user) is 'AnonymousUser':
        return redirect('index')
    subscribers = Subscriber.objects.all()
    for subscriber in subscribers:
        if not subscriber.unsubscribe_id:
            subscriber.create_unsubscribe_id()
    return render(request, 'newsletter/index.html')
