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
    print(subscribers)
    return render(request, 'newsletter/index.html')


def unsubscribe(request, unsubscribe_id):
    try:
        a = Subscriber.objects.get(unsubscribe_id=unsubscribe_id)
        a.subscribed = False
        a.save()
    except Exception:
        print('no user with id' + str(unsubscribe_id))
    return render(request, 'newsletter/unsubscribe_confirmation.html')
