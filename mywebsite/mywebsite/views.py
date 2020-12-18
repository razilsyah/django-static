from django.shortcuts import render


def index(request):
    context = {
        'title': 'HOME',
        'header': 'django-experiment',

    }

    return render(request, 'index.html', context)
