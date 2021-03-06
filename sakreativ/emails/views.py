from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.core.mail import EmailMessage
from blog.models import Customer, ShoppingCart
from newsletter.models import Newsletter, Subscriber
# Create your views here.


def index(request):
    customer = Customer.objects.get(pk=request.COOKIES['customer'])
    shopping_cart = ShoppingCart.objects.get(pk=request.COOKIES['shopping_cart'])
    print(customer.name)
    subject = 'Besten Dank für deine Bestellung'
    mail_from = 'sakrea2019@gmail.com'

    to = [customer.email_address]
    items = shopping_cart.items.all()
    ctx = {
        'customer': customer,
        'shopping_cart': shopping_cart,
        'items': items
    }
    print(items)
    message = get_template('emails/order_confirmation.html').render(ctx)
    msg = EmailMessage(subject, message, to=to, from_email=mail_from)
    msg.content_subtype = 'html'
    msg.send()
    response = render(request, 'emails/sender.html')
    # response.delete_cookie('shopping_cart')
    # response.delete_cookie('customer')

    subject = 'Neue Bestellung von ' + customer.Vorname
    to = ['sara.bahr@gmx.ch']
    message = get_template('emails/new_order.html').render(ctx)
    msg2 = EmailMessage(subject, message, to=to, from_email=mail_from)
    msg2.content_subtype = 'html'
    msg2.send()
    return response


def send_newsletter(request, newsletter_id):
    news = Newsletter.objects.get(pk=newsletter_id)
    news.sent = True
    news.save()
    subscribers = Subscriber.objects.filter(subscribed=True)
    to = []
    for subscriber in subscribers:
        to.append(subscriber.email_address)
    print(to)
    subject = 'Neuer Blog Beitrag: ' + news.blog_post.title
    mail_from = 'Sara von Sakrea <sakrea2019@gmail.com>'
    ctx = {'post': news.blog_post, 'subscriber': ''}

    for subscriber in subscribers:
        ctx['subscriber'] = subscriber
        to = [subscriber.email_address]
        message = get_template('emails/blog_newsletter.html').render(ctx)
        msg = EmailMessage(subject, message, to=to, from_email=mail_from)
        msg.content_subtype = 'html'
        msg.send()

    return redirect('newsletter')
