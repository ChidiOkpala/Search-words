import requests
import json
from django.shortcuts import render
from bs4 import BeautifulSoup
from . import models

BASE_SEARCH_API = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/ImageSearchAPI"
headers = {
	"X-RapidAPI-Key": "d2ec8df260msh935835d9372f62ap1d5933jsna9ac03680531",
	"X-RapidAPI-Host": "contextualwebsearch-websearch-v1.p.rapidapi.com"
}

class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

# Create your views here.
def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)

    querystring = {
      "q":search,
      "pageNumber":"1",
      "pageSize":"10",
      "autoCorrect":"true"
    }
    response = requests.request("GET", BASE_SEARCH_API, headers=headers, params=querystring)
    data = response.text

    d = json.loads(data)
    values = dotdict(d)

    stuff_for_frontend = {
      'search': search,
      'search_result': values.value
    }
    return render(request, 'my_app/new_search.html', stuff_for_frontend)