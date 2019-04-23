from django.shortcuts import render, redirect


# Create your views here.


def index(request):
    if str(request.user) is 'AnonymousUser':
        print(request.user)
        return redirect('index')
    print(request.user)
    return render(request, 'newsletter/index.html')
