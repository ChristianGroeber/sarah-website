from django.shortcuts import render, redirect
from .models import Subscriber, Newsletter
from .forms import SubscriptionForm, CreateNewsletter

# Create your views here.


def index(request):
    if str(request.user) is 'AnonymousUser':
        return redirect('index')
    subscribers = Subscriber.objects.all()
    newsletters = Newsletter.objects.all()
    for subscriber in subscribers:
        if not subscriber.unsubscribe_id:
            subscriber.create_unsubscribe_id()
    if request.method == 'POST':
        form = CreateNewsletter(request.POST)
        print(form)
        news = Newsletter(blog_post=form.cleaned_data['blog_post'])
        news.save()
        print(news)
    form = CreateNewsletter()
    return render(request, 'newsletter/index.html', {'subscribers': subscribers, 'newsletters': newsletters, 'form': form})


def delete_newsletter(request, newsletter_id):
    if str(request.user) is 'AnonymousUser':
        return redirect('index')
    news = Newsletter.objects.get(pk=newsletter_id)
    news.delete()
    return redirect('newsletter')


def unsubscribe(request, unsubscribe_id):
    try:
        a = Subscriber.objects.get(unsubscribe_id=unsubscribe_id)
        a.subscribed = False
        a.save()
    except Exception:
        print('no user with id' + str(unsubscribe_id))
    return render(request, 'newsletter/unsubscribe_confirmation.html')


def subscribe(request):
    form = SubscriptionForm()
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        print(form)
        sub = Subscriber(email_address=form.cleaned_data['email_address'])
        sub.save()
        return redirect('/')
    return render(request, 'newsletter/subscribe.html', {'form': form})


def subscribe_from_url(request, subscriber_mail):
    sub = Subscriber(email_address=subscriber_mail)
    sub.save()
    return redirect('/')
