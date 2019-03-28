from .models import Page


def pages(request):
    ret = {'pages': Page.objects.filter(show_on_page=True, only_show_to_me=False)}
    if not str(request.user) == 'AnonymousUser':
        ret = {'pages': Page.objects.filter(show_on_page=True)}
    return ret

