from django.shortcuts import render

from . import views


def home(request):
    return render (request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    print(search)
    stuff_for_frontend = {
        'search' : search,
    }
    return render(request, 'scrape_app/new_search.html', stuff_for_frontend)
