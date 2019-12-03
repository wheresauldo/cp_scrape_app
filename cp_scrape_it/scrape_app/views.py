from django.shortcuts import render

from . import views


def home(request):
    return render (request, 'base.html')

def new_search(request):
    return render(request, 'cp_scrape_it/new_search.html')
