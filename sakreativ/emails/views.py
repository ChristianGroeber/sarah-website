from django.shortcuts import render
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
# Create your views here.


def index(request):
    subject = 'hello from'
    mail_from = 'sakrea2019@gmail.com'

    to = ['swiss8oy.chg@gmail.com']
    ctx = {
        'user': 'buddy',
        'something': 'something',
    }

    message = get_template('emails/test_template.html').render(ctx)
    msg = EmailMessage(subject, message, to=to, from_email=mail_from)
    msg.content_subtype = 'html'
    msg.send()
    return render(request, 'emails/sender.html')
