from .models import Page


def pages(request):
    return {
        'pages': Page.objects.filter(show_on_page=True)
    }
