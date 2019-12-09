from django.shortcuts import render
import requests

from . import models

from bs4 import BeautifulSoup

from requests.compat import quote_plus

BASE_CRAIGSLIST_URL = 'https://newyork.craigslist.org/search/bbb?query={}'

def home(request):
    return render (request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    print(quote_plus(search))
    final_url =  BASE_CRAIGSLIST_URL.format(quote_plus(search))
    response = requests.get('https://newyork.craigslist.org/search/bbb?query=python&sort=rel')
    data = response.text
    stuff_for_frontend = {
        'search' : search,
    }
    return render(request, 'scrape_app/new_search.html', stuff_for_frontend)
