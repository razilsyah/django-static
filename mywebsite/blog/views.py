from django.shortcuts import render

# Create your views here.


def index(request):

    context = {
        'title': 'BLOG',
        'header': 'welcome to my BLOG',

    }
    return render(request, 'blog/index.html', context)
