from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'ABOUT',
        'header': 'MY ABOUT',

    }
    return render(request, 'about/index.html', context)
